def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    nums = numbers[62:93]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]