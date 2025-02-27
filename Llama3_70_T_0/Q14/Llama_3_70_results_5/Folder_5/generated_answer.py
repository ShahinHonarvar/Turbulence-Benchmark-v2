def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    nums = sorted(numbers[3:6])
    if len(nums) < 2:
        return None
    return nums[1]