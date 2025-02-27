def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    return sorted(sorted_string[:2], reverse=True)