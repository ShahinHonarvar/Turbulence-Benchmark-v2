def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
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

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
                return False
        return True
    x = num_tuple[39]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [n for n in primes if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)