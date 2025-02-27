def find_second_smallest_num(numbers):
    if len(numbers) <= 38:
        return None
    nums = numbers[28:39]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]