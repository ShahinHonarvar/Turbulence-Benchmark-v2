def all_right_truncatable_prime(num_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str) - 1, 0, -1):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = num_tuple[61]
    result = [num for num in range(2, x) if is_right_truncatable(num) and is_prime(num)]
    return sorted(result) if result else []