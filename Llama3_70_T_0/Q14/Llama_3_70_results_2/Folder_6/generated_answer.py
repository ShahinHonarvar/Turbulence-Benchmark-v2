def find_second_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    nums = sorted(numbers[29:80])
    if len(nums) < 2:
        return None
    return nums[1]