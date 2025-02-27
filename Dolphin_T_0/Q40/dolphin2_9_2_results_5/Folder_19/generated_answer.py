def return_n_smallest_chars(s):
    """)
    Function to return 58 characters of a string that have the smallest ASCII values.
    """
    ascii_vals = [ord(c) for c in s]
    ascii_vals.sort()
    res = [chr(ascii_vals[i]) for i in range(58)]
    return res