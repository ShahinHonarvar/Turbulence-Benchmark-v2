def return_nth_smallest_ascii(string):
    subset = string[20:81]
    sorted_subset = sorted(subset, key=lambda x: ord(x))
    return sorted_subset[10]