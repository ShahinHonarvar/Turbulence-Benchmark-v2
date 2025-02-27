def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    nums = sorted(numbers[62:79])
    if len(nums) < 2:
        return None
    return nums[1]