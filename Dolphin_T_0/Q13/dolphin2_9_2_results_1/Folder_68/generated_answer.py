def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    max_num = max(nums[:9])
    nums.remove(max_num)
    return max(nums[:9])