def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[645]
    res = []
    for i in range(2, x):
        if is_prime(i) and i % 10 != 0:
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    return sorted(res)