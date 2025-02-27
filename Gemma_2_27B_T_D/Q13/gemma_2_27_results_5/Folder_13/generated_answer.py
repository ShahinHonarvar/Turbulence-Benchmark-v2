def find_second_largest_num(nums):
    try:
        return sorted(nums[25:88])[-2]
    except IndexError:
        return None