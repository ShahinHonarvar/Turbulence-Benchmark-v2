def find_second_smallest_num(nums):
    sublist = nums[25:53]
    if len(sublist) < 2:
        return None
    sorted_nums = sorted(sublist)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i - 1]:
            return sorted_nums[i]
    return None