def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        d = 3
        while d * d <= n:
            if n % d == 0:
                return False
            d = d + 2
        return True
    x = t[71]
    right_truncatable = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            j = i
            while j != 0:
                if not is_prime(j):
                    break
                j = j // 10
                if j != 0:
                    right_truncatable.append(i)
                    break
    right_truncatable.sort(reverse=True)
    return right_truncatable