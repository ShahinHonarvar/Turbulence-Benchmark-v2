def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[50]
    result = []
    for n in range(x - 1, 0, -1):
        if n % 10 == 0 or not is_prime(n):
            continue
        trunc = n
        while trunc:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            result.append(n)
    return sorted(result, reverse=True)