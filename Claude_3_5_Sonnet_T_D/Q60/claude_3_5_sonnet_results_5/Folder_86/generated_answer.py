def all_left_right_truncatable_prime(tuple_input):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str)):
            left_trunc = int(num_str[i:])
            right_trunc = int(num_str[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    x = tuple_input[126]
    result = []
    for num in range(x, 10, -1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result