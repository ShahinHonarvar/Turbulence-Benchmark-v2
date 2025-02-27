import string

def return_n_smallest_chars(str_of_chars):
    return sorted(str_of_chars, key=ord, reverse=True)[:72][::-1]