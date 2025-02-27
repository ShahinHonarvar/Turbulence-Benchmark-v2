def all_left_right_truncatable_prime(x):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            left = int(str_num[0:i])
            right = int(str_num[i:])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result