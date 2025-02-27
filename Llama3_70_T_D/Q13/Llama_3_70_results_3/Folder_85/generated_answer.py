def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    nums = sorted(numbers[6:9], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]