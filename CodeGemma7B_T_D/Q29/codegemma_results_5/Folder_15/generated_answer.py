def gcf_two_nums(nums):
    length = len(nums)
    if length < 2:
        return 'Needs to be provided with 2 or more numbers!'
    num1, num2 = (nums[0], nums[1])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1