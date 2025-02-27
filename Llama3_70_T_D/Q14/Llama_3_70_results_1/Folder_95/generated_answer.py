def find_second_smallest_num(numbers):
    if len(numbers) < 86:
        return None
    nums = sorted(numbers[75:86])
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]