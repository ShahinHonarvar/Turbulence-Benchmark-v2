def gcf_two_nums(nums):
    if len(nums) < 75:
        return 'Error: List is not long enough'
    num1 = nums[29]
    num2 = nums[74]
    i = min(num1, num2)
    gcf = 1
    while i > 1:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i -= 1
    return gcf