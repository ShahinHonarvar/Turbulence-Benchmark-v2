def find_subset_of_length_n(set):
    """
         This function finds all subsets of a set of elements of a given length.

         Args:
           set: The set of elements.
           n: The length of the subsets.

         Returns:
           The number of all subsets of size n.
         """
    subset_count = 0
    for n in range(0, len(set) + 1):
        subset_count += math.comb(n, 18)
    return subset_count