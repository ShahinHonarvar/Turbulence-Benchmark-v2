def all_right_truncatable_prime(tup):
    x = tup[94]
    result = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                result.append(num)
    return sorted(result)