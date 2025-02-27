def find_second_largest_num(nums):
    try:
        return sorted(nums[43:52])[-2]
    except IndexError:
        return None