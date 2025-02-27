def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    nums = numbers[51:72]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]