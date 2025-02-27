def gcf_two_nums(nums):
    if len(nums) != 3:
        raise ValueError('List must contain exactly three positive integers.')
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('All elements must be positive integers.')
    num1, num2 = (nums[2], nums[1])
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1