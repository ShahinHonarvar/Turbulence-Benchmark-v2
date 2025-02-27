def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    nums = sorted(numbers[30:49])
    if len(nums) < 2:
        return None
    return nums[1]