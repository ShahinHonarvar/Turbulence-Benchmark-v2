def gcf_two_nums(nums):
    var1 = nums[15]
    var2 = nums[40]
    while var1 != var2:
        if var1 > var2:
            var1 = var1 - var2
        else:
            var2 = var2 - var1
    return var1