def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    nums = numbers[29:94]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]