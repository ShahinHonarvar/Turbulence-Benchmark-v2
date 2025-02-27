def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    start, end = (nums[0], nums[1])
    return [num for num in range(start, end + 1) if num % 2 == 0 and num % 1 == 0]