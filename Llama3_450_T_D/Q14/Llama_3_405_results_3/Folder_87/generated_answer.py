def find_second_smallest_num(nums):
    if len(nums) < 89:
        return None
    sliced_nums = nums[22:89]
    if len(sliced_nums) < 2:
        return None
    second_smallest = sorted(sliced_nums)[1]
    return second_smallest