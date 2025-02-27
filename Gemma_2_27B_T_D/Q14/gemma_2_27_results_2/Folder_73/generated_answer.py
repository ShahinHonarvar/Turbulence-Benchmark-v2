def find_second_smallest_num(nums):
    try:
        sorted_slice = sorted(nums[59:98])
        return sorted_slice[1]
    except IndexError:
        return None