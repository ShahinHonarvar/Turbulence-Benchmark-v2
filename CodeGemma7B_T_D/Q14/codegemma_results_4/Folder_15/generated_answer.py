def find_second_smallest_num(numbers):
    if not numbers or not 0 <= len(numbers) <= 3:
        return None
    nums = sorted(numbers)
    second_smallest = nums[1] if len(nums) > 1 else None
    return second_smallest