def find_second_smallest_num(nums):
    try:
        return sorted(nums[3:6])[1]
    except IndexError:
        return None