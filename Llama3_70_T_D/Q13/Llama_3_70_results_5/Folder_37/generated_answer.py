def find_second_largest_num(nums):
    try:
        return sorted(nums[1:6])[-2]
    except IndexError:
        return None