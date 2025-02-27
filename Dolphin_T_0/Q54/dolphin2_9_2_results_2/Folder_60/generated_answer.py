def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable(n):
        if n < 10:
            return True
        return is_prime(n) and is_truncatable(n // 10)
    primes = []
    for num in range(2, x):
        if is_prime(num) and is_truncatable(num):
            primes.append(num)
    return sorted(primes)