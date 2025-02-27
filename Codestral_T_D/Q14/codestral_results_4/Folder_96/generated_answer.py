def find_second_smallest_num(nums):
    sliced_list = sorted(nums[50:201])
    return None if len(sliced_list) < 2 else sliced_list[1]