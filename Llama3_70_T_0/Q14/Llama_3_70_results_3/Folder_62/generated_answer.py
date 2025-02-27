def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    nums = sorted(numbers[10:67])
    if len(nums) < 2:
        return None
    return nums[1]