def find_second_smallest_num(nums):
    sliced_nums = nums[4:9]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]