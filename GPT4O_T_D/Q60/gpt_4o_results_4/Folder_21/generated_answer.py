def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        length = len(str_num)
        for i in range(length):
            left_truncate = int(str_num[i:])
            right_truncate = int(str_num[:length - i])
            if not is_prime(left_truncate) or not is_prime(right_truncate):
                return False
        return True
    x = nums[175]
    return sorted([num for num in range(10, x + 1) if is_left_right_truncatable_prime(num)])