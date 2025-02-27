def find_second_largest_num(nums):
    if len(nums) < 32 or len(nums) < 29:
        return None
    sublist = nums[28:33]
    sublist.sort()
    return sublist[-2]