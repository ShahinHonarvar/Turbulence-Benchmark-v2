def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1 or n <= 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[35]
    L = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            trunc_num = i
            while trunc_num > 0:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                L.append(i)
    return sorted(L, reverse=True)