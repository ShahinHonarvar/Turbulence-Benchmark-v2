def all_ints_not_div_by_num(nums):
    filtered_nums = []
    for num in nums[15:92]:
        if num % 59 != 0:
            filtered_nums.append(num)
    return filtered_nums or []