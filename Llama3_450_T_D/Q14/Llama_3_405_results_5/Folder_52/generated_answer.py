def find_second_smallest_num(nums):
    try:
        nums = sorted(nums[64:67])
        if len(nums) < 2:
            return None
        return nums[1]
    except IndexError:
        return None