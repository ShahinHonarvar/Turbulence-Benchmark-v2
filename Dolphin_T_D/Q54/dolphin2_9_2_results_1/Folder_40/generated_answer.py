def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[10]
    l = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            temp = i
            while temp > 1:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                l.append(i)
    l.sort(reverse=True)
    return l