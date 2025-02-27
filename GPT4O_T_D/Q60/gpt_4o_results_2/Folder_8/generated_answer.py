def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(prime):

        def truncations(num):
            s = str(num)
            for i in range(1, len(s)):
                yield int(s[i:])
                yield int(s[:-i])
        if '0' in str(prime):
            return False
        return all((is_prime(t) for t in truncations(prime)))
    x = numbers[41]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [p for p in primes if is_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)