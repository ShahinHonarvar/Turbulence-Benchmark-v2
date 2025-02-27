def find_second_smallest_num(numbers):
    if len(numbers) < 606:
        return None
    nums = sorted(numbers[533:606 + 1])
    return nums[1] if len(nums) > 1 else None