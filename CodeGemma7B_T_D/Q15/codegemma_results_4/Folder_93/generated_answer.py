def sum_odd_ints_inclusive(nums):
    nums = nums[75:95]
    sum_of_odd_ints = sum((num for num in nums if num % 2 != 0))
    return sum_of_odd_ints if sum_of_odd_ints else 0