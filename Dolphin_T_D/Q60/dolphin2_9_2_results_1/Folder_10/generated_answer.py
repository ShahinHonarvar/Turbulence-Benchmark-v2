def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[38]
    l = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if not is_prime(i):
            continue
        j = i
        while strlen(j) > 1:
            if not is_prime(j):
                break
            j = int(j[1:-1])
        else:
            j = j // 10
        l.append(i)
    return list(reversed(sort(l)))