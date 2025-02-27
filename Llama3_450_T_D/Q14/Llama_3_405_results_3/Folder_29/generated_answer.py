def find_second_smallest_num(nums):
    sliced_nums = nums[55:99]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]