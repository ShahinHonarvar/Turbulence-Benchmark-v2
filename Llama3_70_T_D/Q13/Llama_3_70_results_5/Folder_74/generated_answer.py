def find_second_largest_num(numbers):
    nums = sorted(numbers[17:79], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]