def gcf_three_nums(nums):
    var1 = nums[693]
    var2 = nums[331]
    var3 = nums[668]
    min_val = min(var1, var2, var3)
    while min_val > 0:
        if var1 % min_val == 0 and var2 % min_val == 0 and (var3 % min_val == 0):
            return min_val
        min_val -= 1
    return 1