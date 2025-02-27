def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    nums = sorted(numbers[62:64])
    if len(nums) < 2:
        return None
    return nums[-2]