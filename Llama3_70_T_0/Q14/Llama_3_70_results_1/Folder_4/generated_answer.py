def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    nums = sorted(numbers[70:85])
    if len(nums) < 2:
        return None
    return nums[1]