def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    nums = sorted(numbers[12:93])
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]