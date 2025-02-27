def find_second_smallest_num(nums):
    sublists = nums[10:67]
    unique_nums = list(set(sublists))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]