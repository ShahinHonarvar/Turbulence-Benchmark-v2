def all_odd_ints_exclusive(nums):
    """Write a function called 'all_odd_ints_exclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 44 to index 78, both exclusive. If no odd integers exist in the specified range, the function should return an empty list."""
    out = []
    for num in nums[44:78]:
        if num % 2:
            out.append(num)
    return out