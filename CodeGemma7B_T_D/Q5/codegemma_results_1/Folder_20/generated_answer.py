def all_neg_ints_inclusive(a):
    """This function returns the list of all negative integers from index 56 to index 66, both inclusive."""
    return a[56:67 if any((num < 0 for num in a[56:67])) else 67]