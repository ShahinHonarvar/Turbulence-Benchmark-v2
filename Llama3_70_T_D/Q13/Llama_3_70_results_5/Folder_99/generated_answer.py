def find_second_largest_num(numbers):
    if len(numbers) < 371:
        return None
    nums = sorted(numbers[310:371], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]