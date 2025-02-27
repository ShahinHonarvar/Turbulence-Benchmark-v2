def find_second_smallest_num(numbers):
    if len(numbers) < 751:
        return None
    nums = sorted(numbers[246:751])
    if len(nums) < 2:
        return None
    return nums[1]