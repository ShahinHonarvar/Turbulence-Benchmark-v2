def find_second_smallest_num(nums):
    sub_nums = nums[36:47]
    if len(sub_nums) < 2:
        return None
    else:
        sorted_nums = sorted(set(sub_nums))
        return sorted_nums[1]