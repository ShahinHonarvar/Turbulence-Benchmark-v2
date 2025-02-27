def all_left_right_truncatable_prime(t):

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
        while len(str(n)) > 2:
            if not is_prime(n) or '0' in str(n):
                return False
            n = n // 10
            last_digit = n % 10
            n -= last_digit
            n /= 10
        return is_prime(n)
    x = t[645]
    result = []
    for n in range(2, x + 1):
        if is_truncatable(n):
            result.append(n)
    return sorted(result)