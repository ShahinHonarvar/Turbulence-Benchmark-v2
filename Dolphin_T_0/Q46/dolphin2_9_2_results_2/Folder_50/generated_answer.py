def gcf_three_nums(lst):
    nums = [lst[20], lst[35], lst[74]]
    gcf = nums[0]
    for num in nums[1:]:
        gcf = gcd(gcf, num)
    return gcf