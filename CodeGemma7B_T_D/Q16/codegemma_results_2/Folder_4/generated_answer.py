def sum_even_ints_inclusive(nums):
    """Write a function called 'sum_even_ints_inclusive' that takes one argument, a list of integers, and returns the sum of all even integers from index 12 to index 92, both inclusive. If no even integers exist in the specified range, the function should return 0."""
    sum_even = 0
    for nums in nums[12:93]:
        if nums % 2 == 0:
            sum_even += nums
    return sum_even if sum_even > 0 else 0