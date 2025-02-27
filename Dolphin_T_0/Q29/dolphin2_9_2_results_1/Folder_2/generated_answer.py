def gcf_two_nums(nums):
    if len(nums) < 753:
        return None
    num1 = nums[372]
    num2 = nums[752]
    gcf = min(num1, num2)
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0:
            return gcf
        gcf -= 1
    return None