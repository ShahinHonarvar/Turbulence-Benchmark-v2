def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    nums = numbers[4:9]
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]