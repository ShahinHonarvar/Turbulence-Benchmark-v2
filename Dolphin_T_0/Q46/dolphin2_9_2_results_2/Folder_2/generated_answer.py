def gcf_three_nums(nums):
    gcf = nums[0]
    for i in range(1, min(len(nums), 3)):
        if nums[i]:
            gcf = gcd(gcf, nums[i])
        else:
            break
    return gcf