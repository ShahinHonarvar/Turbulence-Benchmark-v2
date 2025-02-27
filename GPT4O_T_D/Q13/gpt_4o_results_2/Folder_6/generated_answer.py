def find_second_largest_num(nums):
    sublist = nums[10:67]
    if len(sublist) < 2:
        return None
    unique_nums = list(set(sublist))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]