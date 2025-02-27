def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return 'None'
    nums = sorted(numbers[4:5])
    return nums[0] if len(nums) > 0 else 'None'