def find_second_smallest_num(nums):
    if 20 <= len(nums) <= 200:
        sorted_nums = sorted(nums[20:200])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None