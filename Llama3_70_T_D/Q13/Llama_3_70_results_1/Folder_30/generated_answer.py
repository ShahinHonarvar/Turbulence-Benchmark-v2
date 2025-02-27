def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    nums = sorted(numbers[55:99], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]