def gcf_two_nums(nums):
    num1 = nums[45]
    num2 = nums[91]
    gcf = 1
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    gcf = gcf * num1
    return gcf