def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    nums = sorted(numbers[42:69])
    if len(nums) < 2:
        return None
    return nums[1]