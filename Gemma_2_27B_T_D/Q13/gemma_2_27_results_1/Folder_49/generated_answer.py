def find_second_largest_num(nums):
    try:
        return sorted(nums[80:201])[-2]
    except IndexError:
        return None