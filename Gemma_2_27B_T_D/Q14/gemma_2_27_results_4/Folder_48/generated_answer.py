def find_second_smallest_num(nums):
    if len(nums) < 505 or len(set(nums)) != len(nums):
        return None
    sorted_nums = sorted(nums[246:751])
    return sorted_nums[1]