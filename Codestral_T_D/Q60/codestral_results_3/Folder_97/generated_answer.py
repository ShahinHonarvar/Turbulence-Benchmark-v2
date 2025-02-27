def all_left_right_truncatable_prime(tuple_of_numbers):
    x = tuple_of_numbers[645]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])

    def is_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = truncate_left(n)
            if n < 10:
                break
        return is_prime(n)
    result = []
    for i in range(2, x + 1):
        if is_truncatable(i):
            result.append(i)
    return result