def sum_in_range(nums):
    sum_nums = 0
    for num in nums:
        if num >= 136 and num <= 618:
            sum_nums += num
    if sum_nums == 0:
        return 0
    return sum_nums