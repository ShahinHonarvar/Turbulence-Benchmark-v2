def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    sliced_nums = nums[1:9]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]