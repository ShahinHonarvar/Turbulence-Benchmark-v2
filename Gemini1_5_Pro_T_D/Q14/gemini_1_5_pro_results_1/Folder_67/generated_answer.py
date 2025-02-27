def find_second_smallest_num(nums):
    if len(nums) < 55:
        return None
    else:
        sliced_nums = nums[50:55]
        sorted_sliced_nums = sorted(sliced_nums)
        return sorted_sliced_nums[1]