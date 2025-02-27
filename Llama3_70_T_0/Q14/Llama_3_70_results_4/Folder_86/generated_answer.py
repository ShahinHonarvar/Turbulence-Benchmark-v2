def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    nums = sorted(numbers[33:37])
    if len(nums) < 2:
        return None
    return nums[1]