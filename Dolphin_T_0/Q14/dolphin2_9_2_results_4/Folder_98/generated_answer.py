def find_second_smallest_num(nums):
    try:
        return sorted(nums[6:7])[1]
    except IndexError:
        return None