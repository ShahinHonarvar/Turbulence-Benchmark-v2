def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    nums = numbers[80:201]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]