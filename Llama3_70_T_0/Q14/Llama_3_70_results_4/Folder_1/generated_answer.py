def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    nums = sorted(numbers[34:56])
    if len(nums) < 2:
        return None
    return nums[1]