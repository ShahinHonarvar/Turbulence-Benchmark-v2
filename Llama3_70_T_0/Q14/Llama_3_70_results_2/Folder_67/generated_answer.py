def find_second_smallest_num(numbers):
    if len(numbers) < 55:
        return None
    nums = sorted(numbers[50:55])
    if len(nums) < 2:
        return None
    return nums[1]