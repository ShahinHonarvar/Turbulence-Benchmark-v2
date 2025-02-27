def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    nums = sorted(numbers[74:96], reverse=True)
    if len(nums) < 2 or nums[0] == nums[1]:
        return None
    return nums[1]