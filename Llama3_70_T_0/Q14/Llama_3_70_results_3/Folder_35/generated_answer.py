def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    nums = sorted(numbers[15:40])
    if len(nums) < 2:
        return None
    return nums[1]