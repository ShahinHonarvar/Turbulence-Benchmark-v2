def return_n_smallest_chars(input_string):
    unique_chars = list(set(input_string))
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    result = sorted_chars[:85]
    result.sort(reverse=True)
    return result