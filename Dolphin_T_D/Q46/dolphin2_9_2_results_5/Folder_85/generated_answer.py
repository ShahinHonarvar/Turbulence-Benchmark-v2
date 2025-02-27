def gcf_three_nums(lnums):
    gcf_nums = (lnums[49], lnums[46], lnums[13])
    gcf_result = gcf_nums[0]
    for i in range(1, len(gcf_nums)):
        gcf_result = gcd(gcf_result, gcf_nums[i])
    return gcf_result