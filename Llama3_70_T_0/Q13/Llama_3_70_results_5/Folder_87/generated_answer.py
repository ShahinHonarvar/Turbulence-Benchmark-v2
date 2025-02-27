def find_second_largest_num(numbers):
    if len(numbers) < 47:
        return None
    nums = numbers[36:47]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]