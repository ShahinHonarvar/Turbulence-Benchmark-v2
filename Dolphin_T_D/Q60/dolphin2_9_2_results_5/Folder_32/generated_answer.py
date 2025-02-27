def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        while len(str(n)) > 1:
            if str(n)[0] == '0' or str(n)[-1] == '0':
                return False
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    x = t[42]
    l = []
    for i in range(x, 1, -1):
        if is_left_right_truncatable_prime(i):
            l.append(i)
    return l