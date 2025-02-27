def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    nums = sorted(numbers[75:86], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]