def find_second_smallest_num(numbers):
    if len(numbers) <= 8:
        return None
    nums = numbers[6:9]
    nums = sorted(nums)
    return nums[1] if len(nums) > 1 else None