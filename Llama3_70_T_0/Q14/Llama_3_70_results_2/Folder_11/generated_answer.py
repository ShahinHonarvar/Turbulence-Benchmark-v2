def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    nums = sorted(numbers[66:94])
    if len(nums) < 2:
        return None
    return nums[1]