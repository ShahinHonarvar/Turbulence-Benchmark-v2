def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    nums = sorted(numbers[90:100])
    if len(nums) == 1:
        return None
    return nums[1]