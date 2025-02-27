def find_second_smallest_num(nums):
    try:
        return sorted(nums[209:557])[1]
    except IndexError:
        return None