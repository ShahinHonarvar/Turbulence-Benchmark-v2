def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    X = t[89]
    left_truncatable = []
    for num in range(X, 1, -1):
        if '0' in str(num) or not is_prime(num):
            continue
        trunc_num = num
        while trunc_num > 0:
            if not is_prime(trunc_num):
                break
            trunc_num //= 10
        else:
            left_truncatable.append(num)
    return sorted(left_truncatable, reverse=True)