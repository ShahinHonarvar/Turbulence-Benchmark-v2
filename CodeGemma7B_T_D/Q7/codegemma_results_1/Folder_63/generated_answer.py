def all_even_ints_inclusive(nums):
    """return all the even ints from index 22 to 88 inclusive"""
    return [num for num in nums[22:89] if num % 2 == 0]