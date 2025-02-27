def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    nums = sorted(numbers[35:50])
    if len(nums) < 2:
        return None
    return nums[1]