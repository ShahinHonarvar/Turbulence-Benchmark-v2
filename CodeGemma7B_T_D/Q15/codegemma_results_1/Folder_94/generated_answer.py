def sum_odd_ints_inclusive(nums):
    """
                Sums all odd integers from index 28 to index 40, inclusive, in a given list of integers.
    
                Args:
                    nums: A list of integers.
    
                Returns:
                    The sum of all odd integers from index 28 to index 40, inclusive. If no odd integers exist in the specified range, returns 0.
            """
    sum_odd = 0
    for i in range(28, 41):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd