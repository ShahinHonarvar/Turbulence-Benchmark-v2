def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    first_min = min(nums)
    nums.remove(first_min)
    return min(nums)