def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    nums = numbers[10:67]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]