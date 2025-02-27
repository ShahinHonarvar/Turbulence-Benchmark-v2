def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    nums = numbers[35:50]
    if len(nums) < 2:
        return None
    nums.remove(max(nums))
    return max(nums) if nums else None