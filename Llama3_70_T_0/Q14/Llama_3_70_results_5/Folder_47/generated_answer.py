def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    nums = sorted(numbers[22:64])
    if len(nums) < 2:
        return None
    return nums[1]