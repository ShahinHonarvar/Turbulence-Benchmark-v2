def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    max_num = max(nums[0:10])
    nums.remove(max_num)
    second_max_num = max(nums[0:10])
    return second_max_num if second_max_num != max_num else None