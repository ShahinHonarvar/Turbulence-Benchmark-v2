def all_left_right_truncatable_prime(x):
    if not isinstance(x, tuple):
        raise TypeError('Expected a tuple as an argument')
    if len(x) != 1 or x[0] < 1:
        raise ValueError('Expected a tuple with one positive integer as an argument')
    x = x[0]

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

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:i])):
                return False
        return True
    return sorted([p for p in range(x + 1) if is_truncatable_prime(p)])