def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    nums = numbers[1:6]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[-2]