def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    sub_nums = nums[22:51]
    if len(sub_nums) < 2:
        return None
    smallest = min(sub_nums)
    sub_nums_without_smallest = [num for num in sub_nums if num != smallest]
    if sub_nums_without_smallest:
        return min(sub_nums_without_smallest)
    else:
        return None