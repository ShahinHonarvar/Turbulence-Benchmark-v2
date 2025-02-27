def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    nums = sorted(numbers[28:39])
    if len(nums) < 2:
        return None
    return nums[1]