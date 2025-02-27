from sympy import isprime

def composite_nums_between_indices(nums):
    """
    Returns a set of all composite numbers in the given list that are between index 13 to index 68.
    Empty set if no composite number exists in the specified range.
    
    Parameters:
    nums (list): a list of positive integers
    
    Returns:
    set: a set of composite numbers between index 13 to 68 or an empty set if no composite number exists
    """

    def is_composite(n):
        return n > 1 and (not isprime(n))
    return set((i for i in nums[12:69] if is_composite(i)))