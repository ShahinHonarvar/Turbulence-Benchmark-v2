def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[65]
    left_truncatables = []
    for i in range(x, 0, -1):
        if is_prime(i):
            num = i
            while num != 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                left_truncatables.append(i)
    return sorted(left_truncatables, reverse=True)