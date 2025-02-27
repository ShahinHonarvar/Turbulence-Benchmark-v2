def all_right_truncatable_prime(tple):
    x = tple[55]

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:-i])):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)