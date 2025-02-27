def find_second_smallest_num(nums):
    if len(nums) == 0:
        return None
    try:
        return sorted(nums[21:98])[1]
    except IndexError:
        return None