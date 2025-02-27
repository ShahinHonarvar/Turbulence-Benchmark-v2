def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        temp = n
        while temp > 0:
            temp //= 10
            if not is_prime(temp):
                return False
        return True
    x = tup[41]
    result = []
    for i in range(2, x):
        if is_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)