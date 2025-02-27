def find_second_largest_num(nums):
    try:
        return sorted(nums[686:988])[-2]
    except IndexError:
        return None