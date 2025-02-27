def find_second_smallest_num(numbers):
    if len(numbers) < 63 or max(numbers) < 63 or min(numbers) > 78:
        return None
    nums = sorted(numbers)[62:79]
    return nums[1] if len(nums) >= 2 else None