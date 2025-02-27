def find_second_smallest_num(nums):
    if len(nums) < 3:
        sub_nums = nums
    else:
        sub_nums = nums[:3]
    sorted_nums = sorted(sub_nums)
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]