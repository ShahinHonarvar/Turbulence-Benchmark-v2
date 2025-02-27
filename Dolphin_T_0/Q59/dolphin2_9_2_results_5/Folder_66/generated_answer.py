def all_left_truncatable_prime(t):
    x = t[25]

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
    ret = []
    for i in range(3, x):
        if i not in ret and is_prime(i):
            j = 0
            while i >= 10 ** j:
                if j:
                    a = int('1' + str(i), 10)
                else:
                    a = i
                if is_prime(a):
                    j += 1
            if j and j - 1 == len(str(i)):
                ret.append(i)
    return sorted(ret, reverse=True)