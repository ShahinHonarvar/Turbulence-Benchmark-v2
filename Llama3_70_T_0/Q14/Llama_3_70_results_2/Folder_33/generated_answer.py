def find_second_smallest_num(numbers):
    if len(numbers) < 747:
        return None
    nums = sorted(numbers[262:747])
    if len(nums) < 2:
        return None
    return nums[1]