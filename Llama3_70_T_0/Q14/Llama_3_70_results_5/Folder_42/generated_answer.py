def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    nums = sorted(numbers[20:98])
    if len(nums) < 2:
        return None
    return nums[1]