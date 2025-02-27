def find_second_largest_num(nums):
    try:
        nums = sorted(nums[32:36])
        if len(nums) < 2:
            return None
        return nums[-2]
    except IndexError:
        return None