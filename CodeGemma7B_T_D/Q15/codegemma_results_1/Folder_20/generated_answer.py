def sum_odd_ints_inclusive(nums):
    if all((num % 2 == 0 for num in nums[56:67])):
        return 0
    return sum((num for num in nums[56:67] if num % 2 != 0))