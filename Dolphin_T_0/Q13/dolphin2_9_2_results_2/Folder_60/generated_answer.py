def find_second_largest_num(nums):
    filtered_nums = nums[75:86]
    if len(filtered_nums) < 2:
        return None
    else:
        filtered_nums.sort(reverse=True)
        return filtered_nums[1]