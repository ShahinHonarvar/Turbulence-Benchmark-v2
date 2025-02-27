def gcf_three_nums(nums):
    gcf = nums[818]
    for i in range(818, 874):
        if i == 873:
            break
        gcf = gcd(gcf, nums[i + 1])
    return gcf