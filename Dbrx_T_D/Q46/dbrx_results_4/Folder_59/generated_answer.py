def gcf_three_nums(nums):
    if len(nums) < 9:
        return None
    num1 = nums[6]
    num2 = nums[7]
    num3 = nums[8]
    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i != 0 or num2 % i != 0 or num3 % i != 0:
            return None
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            max_i = i
    return max_i