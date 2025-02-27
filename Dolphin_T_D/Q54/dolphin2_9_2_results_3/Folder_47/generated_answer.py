def all_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[49]
    right = [i for i in range(1, x) if is_prime(i)]
    res = []
    for i in right:
        while i:
            i //= 10
            if i in right:
                res.append(i)
            else:
                break
    return sorted(list(set(res)))