def all_odd_ints_inclusive(nums):
    """
            Write a function called 'all_odd_ints_inclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 30 to index 87, both inclusive. If no odd integers exist in the specified range, the function should return an empty list.
            """
    return [num for num in nums[30:88] if num % 2 != 0]