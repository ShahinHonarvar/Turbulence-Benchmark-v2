def find_second_largest_num(nums):
    if len(nums) < 57 or len(nums) > 98:
        return None
    nums.sort()
    return nums[-2]