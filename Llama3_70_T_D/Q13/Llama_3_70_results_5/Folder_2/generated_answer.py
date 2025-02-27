def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    nums = numbers[15:40]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]