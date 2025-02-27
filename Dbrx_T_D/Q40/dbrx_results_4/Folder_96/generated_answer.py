def return_n_smallest_chars(input_string):
    if len(input_string) < 20:
        return sorted(list(input_string), key=ord, reverse=True)
    else:
        return sorted(list(input_string), key=ord, reverse=True)[:20]