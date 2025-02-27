def find_second_largest_num(nums):
    if not nums or len(nums) < 6:
        return None
    nums.sort()
    return nums[-2]