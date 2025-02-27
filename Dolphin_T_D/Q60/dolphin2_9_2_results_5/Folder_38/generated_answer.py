def all_left_right_truncatable_prime(t):

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

    def left_and_right_truncatable(n):
        if n < 10:
            return True
        s = str(n)
        length = len(s)
        for trunc in range(length - 2):
            if not is_prime(int(s[trunc + 1:length])):
                return False
        for i in range(2, length):
            if not is_prime(int(s[0:i])):
                return False
        return True
    x = t[28]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and left_and_right_truncatable(i)])