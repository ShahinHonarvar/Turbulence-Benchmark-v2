import sys

def return_n_smallest_chars(string):
    if sys.version_info[0] < 3:
        return sorted(list(string), key=ord, reverse=True)[:2]
    else:
        return sorted(list(string), key=ord)[::-1][:2]