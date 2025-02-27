def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    nums = sorted(numbers[527:539])
    if len(nums) < 2:
        return None
    return nums[1]