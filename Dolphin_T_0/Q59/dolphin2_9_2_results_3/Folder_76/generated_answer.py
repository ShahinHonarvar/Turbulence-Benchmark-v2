def all_left_truncatable_prime(param):
    x = param

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if s[i] == '0':
                return False
            m = int(s[i:])
            if not is_prime(m):
                return False
        return True
    a = [i for i in range(2, x) if is_truncatable(i) and is_prime(i)]
    return sorted(a, reverse=True)