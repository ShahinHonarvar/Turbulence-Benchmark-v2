def find_second_largest_num(numbers):
    nums = numbers[527:539]
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else 'None'