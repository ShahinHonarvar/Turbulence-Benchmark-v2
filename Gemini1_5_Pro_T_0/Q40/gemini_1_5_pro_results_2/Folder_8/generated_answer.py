def return_n_smallest_chars(s):
    return sorted([x for x in s if ord(x) <= 126][:83])