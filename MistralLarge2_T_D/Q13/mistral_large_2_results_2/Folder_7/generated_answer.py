def find_second_largest_num(nums):
    if len(nums) < 925:
        return None
    sublist = nums[661:925]
    if len(sublist) < 2:
        return None
    second_largest = sorted(sublist)[-2]
    return second_largest