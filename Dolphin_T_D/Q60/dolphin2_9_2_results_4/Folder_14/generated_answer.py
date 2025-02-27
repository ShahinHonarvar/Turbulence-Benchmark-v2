def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_lr_prime(n):
        while n > 2 and n % 10 and (n not in (2, 3)):
            n = n // 10
            if not is_prime(n):
                return False
        s = str(n)
        while len(s) > 2:
            if s[0] == s[-1] == '0':
                return False
            if s[0] == '0' or not is_prime(int(s)):
                return False
            if s[-1] == '0' or not is_prime(int(s[::-1])):
                return False
            s = s[1:-1]
        return True
    return sorted([i for i in range(t[-1], -1, -1) if is_lr_prime(i)], reverse=True)