def find_second_largest_num(numbers):
    if len(numbers) < 201 or not all((isinstance(x, (int, float)) for x in numbers)):
        return None
    nums = sorted(numbers[40:201], reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]