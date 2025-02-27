def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    nums = numbers[19:93]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]