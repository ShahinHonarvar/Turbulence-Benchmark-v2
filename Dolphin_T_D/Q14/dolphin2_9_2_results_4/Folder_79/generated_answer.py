def find_second_smallest_num(nums):
    try:
        return sorted(nums[1:6])[1]
    except IndexError:
        return None