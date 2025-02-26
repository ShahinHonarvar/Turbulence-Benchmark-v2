def return_n_smallest_chars(string):
    if len(string) < 23:
        return sorted(list(string), reverse=True)
    sorted_chars = sorted(string)[:23]
    return sorted(sorted_chars, reverse=True)