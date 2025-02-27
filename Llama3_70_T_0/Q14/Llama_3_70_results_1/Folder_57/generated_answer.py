def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    nums = sorted(numbers[20:31])
    if len(nums) < 2:
        return None
    return nums[1]