def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    nums = sorted(numbers[80:201])
    if len(nums) < 2:
        return None
    return nums[1]