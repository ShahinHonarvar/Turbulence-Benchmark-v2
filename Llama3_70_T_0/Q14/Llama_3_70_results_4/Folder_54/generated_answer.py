def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    nums = sorted(numbers[68:87])
    if len(nums) < 2:
        return None
    return nums[1]