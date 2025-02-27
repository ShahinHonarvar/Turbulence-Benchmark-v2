def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 30:
        return None
    return nums[-2]