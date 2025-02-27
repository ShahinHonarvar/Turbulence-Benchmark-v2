def gcf_three_nums(nums):
    indices = [64, 80, 15]
    values = [nums[i] for i in indices]
    gcf = values[0]
    for num in values:
        while values % num != 0:
            gcf = num
        return gcf