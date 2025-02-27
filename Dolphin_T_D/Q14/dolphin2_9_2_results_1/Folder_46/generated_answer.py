def find_second_smallest_num(nums):
    if 13 <= 68 < len(nums):
        sublist = nums[13:69]
        unique_nums = list(set(sublist))
        sorted_nums = sorted(unique_nums)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None