def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    primes = [2, 3, 5, 7]
    for num in range(10, x):
        if all((int(str(num)[-i]) > 0 for i in range(1, len(str(num)) + 1))):
            if is_prime(num):
                primes.append(num)
    return sorted(primes, reverse=True)