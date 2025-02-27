def all_right_truncatable_prime(nums):
    x = nums[177]
    prime_nums = [num for num in nums if is_prime(num)]
    right_truncatable_nums = []
    for num in prime_nums:
        if is_right_truncatable(num):
            right_truncatable_nums.append(num)
    return sorted(right_truncatable_nums)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        truncated_num = int(str_num[:-i])
        if not is_prime(truncated_num):
            return False
    return True