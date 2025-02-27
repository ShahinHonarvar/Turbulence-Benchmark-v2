def all_right_truncatable_prime(t):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = t[54]
    r = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j > 1 and is_prime(j // 10):
                j //= 10
            if j == 1:
                r.append(i)
    return sorted(r)