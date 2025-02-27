def find_second_smallest_num(nums):
    if len(nums) < 53:
        return None
    else:
        sliced_nums = nums[26:53]
        sorted_nums = sorted(sliced_nums)
        return sorted_nums[1]