def all_ints_not_div_by_num(nums):
    filtered_nums = []
    for num in nums[90:200]:
        if num % -31 != 0:
            filtered_nums.append(num)
    return filtered_nums or []