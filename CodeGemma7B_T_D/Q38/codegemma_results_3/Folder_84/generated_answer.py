def find_subset_of_length_n(s, n):
    """
            Finds the number of subsets of a set of elements with a given length.

            Args:
                s: A set of elements.
                n: The length of the desired subsets.

            Returns:
                The number of subsets of size n.
            """
    total_subsets = 2 ** len(s)
    subsets = [subset for subset in itertools.combinations(s, n)]
    return len(subsets)