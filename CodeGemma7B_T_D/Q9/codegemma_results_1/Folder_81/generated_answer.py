def all_odd_ints_inclusive(nums):
    """Write a function called 'all_odd_ints_inclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 10 to index 100, both inclusive. If no odd integers exist in the specified range, the function should return an empty list."""
    odds = []
    for i in range(10, 101):
        if i % 2 != 0:
            odds.append(i)
    return odds