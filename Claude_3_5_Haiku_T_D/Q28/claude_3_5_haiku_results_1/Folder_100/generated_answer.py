def return_nth_smallest_ascii(string):
    subset = string[5:48]
    sorted_subset = sorted(subset)
    return sorted_subset[12]