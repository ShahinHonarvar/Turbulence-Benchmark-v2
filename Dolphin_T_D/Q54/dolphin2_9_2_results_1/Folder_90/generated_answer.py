def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    x = t[466]
    for i in range(x):
        if is_prime(i):
            tmp = i
            while tmp != 0:
                if not is_prime(tmp):
                    break
                tmp //= 10
                if tmp <= 1:
                    res.append(i)
                    break
    res.sort(reverse=True)
    return res if res else []