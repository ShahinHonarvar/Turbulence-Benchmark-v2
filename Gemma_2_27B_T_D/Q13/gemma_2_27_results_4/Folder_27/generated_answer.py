def find_second_largest_num(nums):
    try:
        return sorted(nums[66:94])[-2]
    except IndexError:
        return None