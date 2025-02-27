def find_second_smallest_num(nums):
    if len(nums) > 7:
        sliced_nums = nums[5:8]
        sorted_nums = sorted(sliced_nums)
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None