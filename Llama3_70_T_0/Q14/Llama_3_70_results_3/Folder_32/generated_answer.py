def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    nums = sorted(numbers[32:36])
    if len(nums) < 2:
        return None
    return nums[1]