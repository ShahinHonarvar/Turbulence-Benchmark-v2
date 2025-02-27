from sympy import isprime

def composite_nums_between_indices(nums):
    """We start by importing the sympy module, which provides us with a function isprime() that we can use to check if a number is a prime number (i.e., not a composite number)."""
    'Next, we use list comprehension to generate a list of all the numbers in the range from index 75 to index 94, inclusive, that are not prime.'
    return set((num for i, num in enumerate(nums[75:95]) if not isprime(num)))