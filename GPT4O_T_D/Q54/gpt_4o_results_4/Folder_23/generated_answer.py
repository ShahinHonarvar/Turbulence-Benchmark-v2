def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n):
        current = n
        while current > 0:
            if not is_prime(current):
                return False
            current //= 10
        return True
    if len(tup) <= 77:
        return []
    x = tup[77]
    truncatable_primes = []
    for num in range(x):
        if is_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)