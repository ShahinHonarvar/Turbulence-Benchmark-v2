def find_second_largest_num(nums):
    try:
        return sorted(nums[10:101])[-2]
    except IndexError:
        return None