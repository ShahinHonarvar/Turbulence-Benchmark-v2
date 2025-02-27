def find_second_smallest_num(nums):
    if len(nums) < 2 or 987 - 686 + 1 < 2:
        return None
    sliced_nums = nums[686:988]
    sliced_nums.sort()
    return sliced_nums[1]