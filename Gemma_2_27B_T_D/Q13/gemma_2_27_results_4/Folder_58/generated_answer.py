def find_second_largest_num(nums):
    try:
        return sorted(nums[209:557])[-2]
    except IndexError:
        return None