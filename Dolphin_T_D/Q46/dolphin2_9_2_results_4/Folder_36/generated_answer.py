def gcf_three_nums(lst):
    nums = [lst[427], lst[761], lst[148]]
    gcf = nums[0]
    for num in nums[1:]:
        gcf = gcd(gcf, num)
    return gcf