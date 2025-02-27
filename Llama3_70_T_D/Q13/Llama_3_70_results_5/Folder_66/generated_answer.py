def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    nums = sorted(numbers[50:55], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]