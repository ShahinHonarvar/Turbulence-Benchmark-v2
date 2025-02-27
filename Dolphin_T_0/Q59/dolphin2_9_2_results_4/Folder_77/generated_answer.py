def all_left_truncatable_prime(tuple_of_int):

    def is_prime(num):
        if num in (0, 1):
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        if num in (0, 1):
            return True
        if num % 10 == 0:
            return False
        return is_left_truncatable(num // 10) and is_prime(num)
    x = tuple_of_int[767]
    return sorted([i for i in range(x - 1, 1, -1) if is_left_truncatable(i) and is_prime(i)], reverse=True)