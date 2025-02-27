def all_right_truncatable_prime(numbers):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(primes, num):
        if len(primes) == 0:
            return is_prime(num)
        for prime in primes:
            if int(num * 10) == prime:
                return False
        comp = [int(num / 10 ** i) for i in range(0, len(str(num)))]
        return all(map(is_prime, comp))
    primes = [2, 3, 5, 7]
    right = []
    for num in range(11, numbers[30]):
        if is_prime(num) and is_truncatable_prime(primes, num):
            primes.append(num)
            right.append(num)
    return sorted(right)