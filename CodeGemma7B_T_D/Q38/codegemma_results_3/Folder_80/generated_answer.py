def find_subset_of_length_n(subset_set):
    """
   counts the number of subsets of size n
   
   time complexity: O(2^n)
   """
    n = len(subset_set)
    power_set = 2 ** n
    result = power_set
    return result