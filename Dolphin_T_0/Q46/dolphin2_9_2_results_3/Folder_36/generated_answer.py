def gcf_three_nums(nums_list):
    gcf = nums_list[427]
    for i in range(427, 149, -1):
        gcf = math.gcd(gcf, nums_list[i])
    return gcf