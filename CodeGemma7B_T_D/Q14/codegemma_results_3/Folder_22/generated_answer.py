def find_second_smallest_num(nums):
    nums = nums[40:201]
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]