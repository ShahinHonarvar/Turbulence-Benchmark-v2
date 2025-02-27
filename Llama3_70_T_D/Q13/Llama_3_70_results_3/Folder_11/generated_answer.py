def find_second_largest_num(numbers):
    if 51 < len(numbers):
        nums = numbers[37:52]
        if len(nums) > 1:
            largest = max(nums)
            second_largest = max((num for num in nums if num != largest))
            return second_largest
    return None