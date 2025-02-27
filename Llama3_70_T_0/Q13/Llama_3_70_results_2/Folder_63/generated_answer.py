def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    nums = numbers[22:89]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]