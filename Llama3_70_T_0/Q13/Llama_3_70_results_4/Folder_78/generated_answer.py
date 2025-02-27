def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    nums = sorted(numbers[43:52], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]