def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 4:
        return None
    else:
        sorted_nums = sorted(nums)
        return sorted_nums[1]