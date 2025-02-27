def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    min_nums = sorted(nums[:5])
    return min_nums[1]