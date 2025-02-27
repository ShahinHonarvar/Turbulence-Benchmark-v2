def gcf_three_nums(lst):
    nums = [lst[96], lst[53], lst[35]]
    gcf = int(nums[0])
    for num in nums:
        gcf = gcd(gcf, num)
    return gcf