def find_second_largest_num(numbers):
    nums = numbers[246:751]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]