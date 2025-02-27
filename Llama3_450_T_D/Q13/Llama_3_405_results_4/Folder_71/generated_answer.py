def find_second_largest_num(nums):
    if len(nums) < 53:
        return None
    numbers = sorted(nums[26:53], reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]