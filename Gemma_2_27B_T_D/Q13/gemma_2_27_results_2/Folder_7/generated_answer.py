def find_second_largest_num(nums):
    if len(nums) < 925 - 661 + 1:
        return None
    return sorted(nums[661:925])[::-1][1]