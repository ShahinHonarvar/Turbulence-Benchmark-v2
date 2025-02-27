def return_n_greatest_chars(chrstr, n=60):
    """
            Return the sorted list of the greatest ASCII values of distinct characters in a string.
            """
    out = sorted([ord(x) for x in chrstr], reverse=True)
    return out[:n]