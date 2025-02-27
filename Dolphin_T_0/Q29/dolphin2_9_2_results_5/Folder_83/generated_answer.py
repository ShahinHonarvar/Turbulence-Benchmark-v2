def gcf_two_nums(nums):
    if len(nums) < 21:
        return 'List must contain at least 21 elements'
    num1 = nums[17]
    num2 = nums[20]
    i = min(num1, num2)
    while i > 1:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return 1