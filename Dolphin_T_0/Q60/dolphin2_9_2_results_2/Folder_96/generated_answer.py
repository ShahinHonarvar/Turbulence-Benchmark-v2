def all_left_right_truncatable_prime(t):

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

    def is_left_right_truncatable_prime(n):
        n = str(n)
        while len(n) > 2:
            if n[0] == '0' or n[-1] == '0':
                return False
            if not is_prime(int(n)):
                return False
            n = n[1:-1]
        if n[0] == '0' or n[-1] == '0' or (not is_prime(int(n))):
            return False
        return True
    x = t[29]
    return sorted(set(filter(is_left_right_truncatable_prime, range(x + 1))))