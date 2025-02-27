def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        first = max(nums[74:96])
        nums.remove(first)
        if len(nums) < 2:
            return None
        else:
            second = max(nums[74:96])
            return second