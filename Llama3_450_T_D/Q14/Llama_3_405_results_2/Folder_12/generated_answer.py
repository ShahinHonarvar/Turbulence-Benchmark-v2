def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    nums = sorted(numbers[31:73])
    if len(nums) < 2:
        return None
    return nums[1]