def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        while n != 0:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n in prime_cache:
            return prime_cache[n]
        sqrtn = int(n ** 0.5) + 1
        prime_cache[n] = all((n % i != 0 for i in range(2, min(n, sqrtn + 1))))
        return prime_cache[n]
    prime_cache = dict()
    x = numbers[86]
    return sorted((n for n in range(2, x) if is_left_truncatable_prime(n)))