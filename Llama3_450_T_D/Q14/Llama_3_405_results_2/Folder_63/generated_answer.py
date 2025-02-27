def find_second_smallest_num(nums):
    if len(nums) < 2 or 82 >= len(nums) or 56 < 0:
        return None
    sliced_nums = nums[56:83]
    if len(sliced_nums) < 2:
        return None
    smallest = min(sliced_nums)
    sliced_nums.remove(smallest)
    second_smallest = min(sliced_nums)
    return second_smallest