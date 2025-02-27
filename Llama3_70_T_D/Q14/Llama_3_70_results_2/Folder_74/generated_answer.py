def find_second_smallest_num(numbers):
    if 36 >= len(numbers) or 46 >= len(numbers):
        return None
    nums = sorted(numbers[36:47])
    if len(nums) < 2:
        return None
    return nums[1]