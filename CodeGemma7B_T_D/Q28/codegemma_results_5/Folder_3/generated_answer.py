def return_nth_smallest_ascii(str_in):
    """Function to find the nth smallest ASCII value in a string."""
    str_slice = str_in[25:46]
    str_sorted = sorted(str_slice)
    return str_sorted[10]