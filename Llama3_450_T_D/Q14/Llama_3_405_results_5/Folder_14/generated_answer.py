def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    nums = sorted(numbers[8:10])
    if len(nums) < 2:
        return None
    return nums[1]