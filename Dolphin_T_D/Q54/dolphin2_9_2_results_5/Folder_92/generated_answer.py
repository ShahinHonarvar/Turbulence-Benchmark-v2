def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[7]
    ret = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j //= 10
            else:
                ret.append(i)
    return sorted(ret)