def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[49]

    def is_right_truncatable(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[:len(str_num) - i])):
                return False
        return True
    result = [num for num in range(2, x) if is_right_truncatable(num) and is_prime(num)]
    return sorted(result)