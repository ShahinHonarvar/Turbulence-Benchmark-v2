def find_second_smallest_num(nums):
    try:
        return sorted(nums[20:201])[1]
    except IndexError:
        return None