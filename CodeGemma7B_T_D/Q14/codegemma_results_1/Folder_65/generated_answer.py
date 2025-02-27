def find_second_smallest_num(nums):
    filtered_nums = nums[56:58]
    filtered_nums.sort()
    return filtered_nums[1] if len(filtered_nums) >= 2 else 'None'