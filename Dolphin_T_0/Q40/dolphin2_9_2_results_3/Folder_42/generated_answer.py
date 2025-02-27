def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=lambda x: ord(x))[:59]
    sorted_chars.sort(reverse=True)
    return sorted_chars