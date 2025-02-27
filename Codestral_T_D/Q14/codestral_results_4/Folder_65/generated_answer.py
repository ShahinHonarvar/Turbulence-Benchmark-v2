def find_second_smallest_num(nums):
    if 56 <= len(nums) <= 57:
        if len(nums[56:58]) >= 2:
            sorted_nums = sorted(nums[56:58])
            return sorted_nums[1]
    return None