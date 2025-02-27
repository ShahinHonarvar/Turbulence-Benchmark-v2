def return_n_smallest_chars(string):
    if len(string) > 84:
        string = sorted(string)[:84]
    else:
        string = sorted(string)
    return sorted(string, reverse=True)