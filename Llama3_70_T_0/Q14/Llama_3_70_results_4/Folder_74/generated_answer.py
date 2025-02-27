def find_second_smallest_num(numbers):
    if len(numbers) < 47:
        return None
    nums = sorted(numbers[36:47])
    if len(nums) < 2:
        return None
    return nums[1]