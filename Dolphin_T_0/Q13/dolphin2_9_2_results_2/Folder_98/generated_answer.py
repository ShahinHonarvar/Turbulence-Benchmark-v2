def find_second_largest_num(nums):
    if len(nums) <= 6:
        max_num = max(nums)
        nums.remove(max_num)
        if len(nums) == 0:
            return None
        else:
            return max(nums)
    else:
        return None