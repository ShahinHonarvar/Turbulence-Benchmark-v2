def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s) - 1):
            if s[i] == '0' or not is_prime(int(s[i:])):
                return False
        return True
    x = t[73]
    l = [i for i in range(2, x) if is_truncatable(i)]
    return sorted(l, reverse=True)