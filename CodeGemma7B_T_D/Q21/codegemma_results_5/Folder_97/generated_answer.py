def all_ints_div_by_num(nums):
    if not nums:
        return []
    filtered_nums = []
    for num in nums[17:64]:
        if num % 89 == 0:
            filtered_nums.append(num)
    return filtered_nums