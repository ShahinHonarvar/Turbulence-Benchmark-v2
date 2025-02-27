def gcf_three_nums(lst):
    nums = [lst[18], lst[37], lst[43]]
    gcf = nums[0]
    for i in nums[1:]:
        while i != 0 and gcf != 0:
            if i > gcf:
                i %= gcf
            elif gcf > i:
                gcf %= i
    return gcf