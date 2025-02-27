def gcf_two_nums(nums):
    num1, num2 = (nums[88], nums[35])
    gcftwo = max(num1, num2)
    while num1 != num2:
        if num1 != 0:
            num2, num1 = (num1, num2 % num1)
        else:
            gcftwo = -1
            break
    return gcftwo