def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if str_n[i] == '0':
                return False
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = t[3]
    res = [i for i in range(x - 1, 1, -1) if is_prime(i) and is_left_truncatable(i)]
    return res