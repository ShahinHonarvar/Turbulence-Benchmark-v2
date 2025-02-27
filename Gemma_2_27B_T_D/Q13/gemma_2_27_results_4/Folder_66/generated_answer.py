def find_second_largest_num(nums):
    try:
        return sorted(nums[50:55])[-2]
    except IndexError:
        return None