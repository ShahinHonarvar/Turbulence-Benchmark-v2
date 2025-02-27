def find_second_smallest_num(numbers):
    if len(numbers) < 72:
        return None
    nums = sorted(numbers[51:72])
    if len(nums) < 2:
        return None
    return nums[1]