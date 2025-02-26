def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    result = sorted_chars[:26] if len(sorted_chars) >= 26 else sorted_chars
    return sorted(result, reverse=True)