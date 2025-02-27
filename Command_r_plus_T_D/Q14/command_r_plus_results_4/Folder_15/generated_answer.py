def find_second_smallest_num(nums):
    smallest_nums = sorted(nums[:4])
    if len(smallest_nums) < 2:
        return None
    return smallest_nums[1]