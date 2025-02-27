def find_second_largest_num(numbers):
    if len(numbers) < 73:
        return None
    nums = numbers[31:73]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]