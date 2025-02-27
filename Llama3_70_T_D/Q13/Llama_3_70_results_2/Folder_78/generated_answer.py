def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    nums = sorted(numbers[43:52], reverse=True)
    return nums[1] if len(nums) > 1 else None