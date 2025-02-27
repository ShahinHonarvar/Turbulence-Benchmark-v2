def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    first_largest = max(nums[0], nums[1])
    second_largest = min(nums[0], nums[1])
    return second_largest