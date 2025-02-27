def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    nums = numbers[40:81]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return nums[1]