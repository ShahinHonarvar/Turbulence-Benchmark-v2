def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    nums = sorted(numbers[25:60])
    if len(nums) < 2:
        return None
    return nums[1]