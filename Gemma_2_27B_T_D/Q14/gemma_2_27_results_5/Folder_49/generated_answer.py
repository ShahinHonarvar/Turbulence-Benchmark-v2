def find_second_smallest_num(nums):
    if len(nums) < 2 or 80 >= len(nums) or 200 >= len(nums):
        return None
    sorted_nums = sorted(nums[80:201])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]