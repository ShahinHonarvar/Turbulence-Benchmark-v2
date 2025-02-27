def all_right_truncatable_prime(num_tuple):
    x = num_tuple[14]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_r_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:-i])):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_prime(num) and is_r_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result