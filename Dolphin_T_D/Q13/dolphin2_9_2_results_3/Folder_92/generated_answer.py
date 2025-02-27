def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) == 0:
        return None
    else:
        return max(nums)