def find_second_smallest_num(nums):
    if len(nums) < 73:
        return None
    else:
        sliced_nums = nums[31:73]
        sorted_nums = sorted(sliced_nums)
        return sorted_nums[1]