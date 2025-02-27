def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        s = str(n)
        for i in range(len(s) - 1):
            if s[0] == '0' or not is_prime(int(s[i:])):
                return False
        return True
    x = t[87]
    return sorted([i for i in range(1, x) if is_truncatable(i)])