def find_second_smallest_num(numbers):
    if len(numbers) < 99:
        return None
    nums = sorted(numbers[55:99])
    if len(nums) < 2:
        return None
    return nums[1]