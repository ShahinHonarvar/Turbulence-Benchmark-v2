def all_ints_div_by_num(nums):
    if not nums or len(nums) < 20:
        return []
    filtered_nums = []
    for i in range(20, 200 + 1):
        if nums[i] % 4 == 0:
            filtered_nums.append(nums[i])
    return filtered_nums