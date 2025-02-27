def find_second_largest_num(numbers):
    if len(numbers) < 35:
        return None
    nums = numbers[32:36]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    if len(nums) > 1:
        return nums[1]
    return None