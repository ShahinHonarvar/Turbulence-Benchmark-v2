def all_left_right_truncatable_prime(num):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                return False
        return True

    def get_truncatable(num):
        str_num = str(num)
        truncatable = [num]
        for i in range(1, len(str_num)):
            if str_num[i:] == '0' or not is_prime(int(str_num[:i])):
                return []
            truncatable.append(int(str_num[:i]))
        return truncatable
    result = []
    for i in range(2, num // 2 + 1):
        if is_prime(i):
            truncatable = get_truncatable(i)
            if truncatable:
                result.extend(truncatable)
    result.sort()
    return result