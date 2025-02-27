def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    res = []
    x = t[92]
    for num in range(2, x):
        if is_prime(num):
            k = num
            while k > 0:
                if not is_prime(k):
                    break
                k //= 10
                if k == 0:
                    res.append(num)
    return sorted(res)