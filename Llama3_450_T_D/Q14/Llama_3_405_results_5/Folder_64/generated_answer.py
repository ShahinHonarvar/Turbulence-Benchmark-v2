def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    first_five_nums = sorted(nums[:5])
    if len(first_five_nums) < 2:
        return None
    return first_five_nums[1]