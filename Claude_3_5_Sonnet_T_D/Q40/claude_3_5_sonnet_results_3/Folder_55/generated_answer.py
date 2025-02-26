def return_n_smallest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, key=ord)
    result = sorted_chars[:75]
    result.sort(reverse=True)
    return result if len(result) == 75 else result + [''] * (75 - len(result))