def return_n_greatest_chars(input_string):
    if len(input_string) < 43:
        return sorted(list(input_string), key=ord, reverse=True)
    else:
        sort_chars = sorted(list(input_string), key=ord, reverse=True)[:43]
        return sort_chars