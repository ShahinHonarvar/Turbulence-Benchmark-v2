def find_second_largest_num(nums):
    try:
        return sorted(nums[68:87])[-2]
    except IndexError:
        return None