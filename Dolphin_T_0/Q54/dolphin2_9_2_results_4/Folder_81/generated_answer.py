def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[98]
    res = [2]
    for i in range(3, x):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j // 10):
                    break
                j //= 10
            else:
                res.append(i)
    return sorted(res)