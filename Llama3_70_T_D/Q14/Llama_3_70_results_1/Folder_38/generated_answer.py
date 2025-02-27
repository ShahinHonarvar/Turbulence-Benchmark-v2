def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    nums = numbers[37:52]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]