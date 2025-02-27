def sum_ints_div_by_either_nums(nums):
    selected_nums = []
    for i in range(78, 82):
        if nums[i] % 76 == 0 or nums[i] % 60 == 0:
            selected_nums.append(nums[i])
    sum_nums = sum(selected_nums)
    if not selected_nums:
        return 0
    return sum_nums