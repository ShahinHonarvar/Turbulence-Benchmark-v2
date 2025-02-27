def all_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = n_tuple[4]
    result = []
    for num in range(x - 1, 1, -1):
        trunc = num
        while trunc > 1:
            if not is_prime(trunc):
                break
            trunc //= 10
        if trunc == 1:
            result.append(num)
    return sorted(result)