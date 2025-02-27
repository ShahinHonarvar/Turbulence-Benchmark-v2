def all_left_right_truncatable_prime(n):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [2, 3, 5, 7]
    for num in range(11, n + 1):
        if is_prime(num):
            primes.append(num)
    return [prime for prime in primes if min(map(int, str(prime))) > 0 and all(is_prime(''.join(filter(len, str(num))))) for num in range(2, n + 1)]