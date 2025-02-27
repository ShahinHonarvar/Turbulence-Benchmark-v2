def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[92]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        num_str = str(num)
        while len(num_str) > 2:
            if len(num_str) == 2:
                if not is_prime(int(num_str)):
                    return False
            elif not is_prime(int(num_str[1:])) or not is_prime(int(num_str[:-1])):
                return False
            num_str = num_str[1:-1]
        return True
    return sorted([i for i in range(x, 1, -1) if is_prime(i) and is_truncatable(i)])