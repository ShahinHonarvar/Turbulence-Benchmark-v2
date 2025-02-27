def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    nums = numbers[37:77]
    nums.sort(reverse=True)
    if len(nums) > 1:
        return nums[1]
    else:
        return None