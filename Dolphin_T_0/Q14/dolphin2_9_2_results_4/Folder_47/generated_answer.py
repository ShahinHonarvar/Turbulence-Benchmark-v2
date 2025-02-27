def find_second_smallest_num(nums):
    sublist = nums[22:64]
    if len(sublist) < 2:
        return None
    smallest_num = min(sublist)
    second_smallest_num = min((num for num in sublist if num > smallest_num))
    return second_smallest_num