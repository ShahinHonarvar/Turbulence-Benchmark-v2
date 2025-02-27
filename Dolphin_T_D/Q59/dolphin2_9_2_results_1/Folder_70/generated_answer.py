def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p ** 2 <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if n_str[i] == '0':
                return False
            if not is_prime(int(n_str[i:] + n_str[:i])):
                return False
        return True
    x = t[433]
    return sorted([i for i in range(2, x) if is_truncatable(i)], reverse=True)