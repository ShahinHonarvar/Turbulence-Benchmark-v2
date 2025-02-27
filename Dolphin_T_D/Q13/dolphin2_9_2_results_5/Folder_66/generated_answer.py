def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    nums = nums[50:55]
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]