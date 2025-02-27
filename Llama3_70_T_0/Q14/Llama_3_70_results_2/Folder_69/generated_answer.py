def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    nums = sorted(numbers[25:88])
    if len(nums) < 2:
        return None
    return nums[1]