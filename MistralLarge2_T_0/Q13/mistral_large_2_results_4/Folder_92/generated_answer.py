def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first, second = (nums[0], nums[1])
    if first < second:
        first, second = (second, first)
    return second