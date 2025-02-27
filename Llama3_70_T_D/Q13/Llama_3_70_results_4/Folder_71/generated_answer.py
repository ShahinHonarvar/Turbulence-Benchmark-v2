def find_second_largest_num(nums):
    try:
        nums = sorted(nums[26:53], reverse=True)
        return nums[1]
    except IndexError:
        return None