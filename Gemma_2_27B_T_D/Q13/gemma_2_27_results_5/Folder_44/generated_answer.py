def find_second_largest_num(nums):
    try:
        return sorted(nums[13:69])[-2]
    except IndexError:
        return None