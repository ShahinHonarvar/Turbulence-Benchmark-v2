def gcf_three_nums(nums):
    fac_list = []
    for i in [8, 9, 3]:
        for j in range(2, nums[i] + 1):
            if nums[i] % j == 0:
                fac_list.append(j)
    return max(fac_list)