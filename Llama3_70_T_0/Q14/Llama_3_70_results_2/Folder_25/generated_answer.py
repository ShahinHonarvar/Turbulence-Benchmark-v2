def find_second_smallest_num(numbers):
    if len(numbers) < 77:
        return None
    nums = sorted(numbers[37:77])
    if len(nums) < 2:
        return None
    return nums[1]