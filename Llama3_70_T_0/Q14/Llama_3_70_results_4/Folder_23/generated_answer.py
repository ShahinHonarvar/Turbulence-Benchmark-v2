def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    nums = sorted(numbers[19:93])
    if len(nums) < 2:
        return None
    return nums[1]