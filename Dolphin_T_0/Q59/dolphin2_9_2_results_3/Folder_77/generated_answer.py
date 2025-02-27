def all_left_truncatable_prime(int_tuple):
    x = int_tuple[767]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_left_truncatable(n):
        if n <= 1:
            return False
        if n <= 4:
            return True
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if is_left_truncatable(i) and is_prime(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes