def find_second_largest_num(nums):
    try:
        nums = sorted(nums[50:55])
        if len(nums) < 2:
            return None
        else:
            return nums[-2]
    except IndexError:
        return None