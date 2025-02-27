def gcf_two_nums(nums):
    num1 = nums[64]
    num2 = nums[80]
    a, b = (max(num1, num2), min(num1, num2))
    while b != 0:
        a, b = (b, a % b)
    return a