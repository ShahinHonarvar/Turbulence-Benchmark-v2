def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    nums = sorted(numbers[5:8])
    if len(nums) < 2:
        return None
    return nums[1]