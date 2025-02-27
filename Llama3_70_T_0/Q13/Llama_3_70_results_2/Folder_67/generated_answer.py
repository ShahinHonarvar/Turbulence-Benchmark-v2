def find_second_largest_num(numbers):
    if len(numbers) < 51:
        return None
    nums = sorted(numbers[22:51], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]