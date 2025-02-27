def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    nums = sorted(numbers[22:89])
    if len(nums) < 2:
        return None
    return nums[1]