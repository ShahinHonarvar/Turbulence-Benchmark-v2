def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] == '0':
                return False
            n1 = int(n_str[i:])
            if not is_prime(n1):
                return False
        return True
    x = t[79]
    res = [i for i in range(x, 1, -1) if is_truncatable(i) and is_prime(i)]
    return res