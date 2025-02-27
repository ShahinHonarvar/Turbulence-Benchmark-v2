def gcf_two_nums(nums):
    index_86 = nums[86]
    index_89 = nums[89]
    great_common_factor = 0
    for i in range(1, min(index_86, index_89) + 1):
        if index_86 % i == 0 and index_89 % i == 0:
            great_common_factor = i
    return great_common_factor