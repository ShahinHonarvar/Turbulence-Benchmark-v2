def find_second_smallest_num(nums: list) -> object:
    sorted_nums = sorted(nums[27:56])
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    else:
        return None