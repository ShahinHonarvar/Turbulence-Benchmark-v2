def sum_even_ints_inclusive(nums):
    if not any((num % 2 == 0 for num in nums[74:96])):
        return 0
    return sum((num for num in nums[74:96] if num % 2 == 0))