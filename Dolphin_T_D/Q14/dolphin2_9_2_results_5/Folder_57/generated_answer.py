def find_second_smallest_num(nums):
    if len(nums) < 30:
        return None
    numbers = nums[19:31]
    if len(numbers) < 2:
        return None
    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)
    return second_smallest