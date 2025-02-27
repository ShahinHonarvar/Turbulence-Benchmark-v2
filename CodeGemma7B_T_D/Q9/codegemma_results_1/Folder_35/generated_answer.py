def all_odd_ints_inclusive(nums):
    """
            Write a function called 'all_odd_ints_inclusive' that takes one argument, a list of integers, and returns the list of all odd integers from index 30 to index 48, both inclusive. If no odd integers exist in the specified range, the function should return an empty list.
            """
    odd_nums = []
    for i in range(30, 49):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    return odd_nums