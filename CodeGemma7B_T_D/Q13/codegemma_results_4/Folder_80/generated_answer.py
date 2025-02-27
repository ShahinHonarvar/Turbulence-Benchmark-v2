def find_second_largest_num(nums):
    nums_limited = nums[64:67]
    sorted_nums = sorted(nums_limited, reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else 'None'