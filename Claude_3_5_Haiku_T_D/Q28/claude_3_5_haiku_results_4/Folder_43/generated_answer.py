def return_nth_smallest_ascii(string):
    substring = string[14:36]
    sorted_subset = sorted(substring)
    return sorted_subset[10]