def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[41]
    left_truncatable_primes = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)