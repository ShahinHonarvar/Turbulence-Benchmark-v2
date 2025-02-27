def all_odd_ints_inclusive(nums):
    """
            Write a function called 'all_odd_ints_inclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 91 to index 99, both inclusive. If no odd integers exist in the specified range, the function should return an empty list.
            """
    out = []
    for num in nums[91:99 + 1]:
        if num % 2 != 0:
            out.append(num)
    return out