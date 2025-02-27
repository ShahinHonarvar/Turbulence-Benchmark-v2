def gcf_three_nums(nums):
    num1 = nums[10]
    num2 = nums[55]
    num3 = nums[36]
    while num2 != num3:
        if num2 > num3:
            num2 = num2 - num3
        else:
            num3 = num3 - num2
    gcf = num1 // num2
    return gcf