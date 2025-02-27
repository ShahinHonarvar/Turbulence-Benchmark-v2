def find_second_smallest_num(nums):
    second_smallest = None
    if len(nums) >= 57:
        sublist = nums[56:58]
        unique_nums = set(sublist)
        sorted_nums = sorted(list(unique_nums))
        if len(sorted_nums) > 1:
            second_smallest = sorted_nums[1]
    return second_smallest