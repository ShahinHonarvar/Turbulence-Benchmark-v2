from sys import maxsize as max_int

def return_n_smallest_chars(message):
    all_chars = list(message)
    all_chars.sort(key=ord)
    return all_chars[:11]