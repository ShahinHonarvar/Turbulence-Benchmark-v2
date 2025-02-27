def find_second_smallest_num(numbers):
    if len(numbers) < 22 or len(numbers) - 1 > 50:
        return 'None'
    nums = numbers[22:51]
    nums.sort()
    return nums[1] or 'None'