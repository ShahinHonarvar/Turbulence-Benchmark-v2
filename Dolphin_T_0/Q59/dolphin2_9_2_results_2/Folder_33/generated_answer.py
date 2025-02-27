def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    x = num_tuple[945]
    result = []
    for num in range(x - 1, 0, -1):
        if is_prime(num):
            trunc = num
            while trunc > 0 and is_prime(trunc):
                trunc //= 10
            if trunc == 0:
                result.append(num)
    return sorted(result, reverse=True)