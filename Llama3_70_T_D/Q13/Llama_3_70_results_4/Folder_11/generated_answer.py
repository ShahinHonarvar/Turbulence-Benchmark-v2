def find_second_largest_num(numbers):
    if len(numbers) <= 51:
        return None
    nums = numbers[37:52]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]