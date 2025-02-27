def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    nums = numbers[90:100]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]