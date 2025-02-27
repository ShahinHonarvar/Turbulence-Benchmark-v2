from itertools import islice

def return_nth_smallest_ascii(str):
    str_iterator = iter(str)
    str_slice = islice(str_iterator, 38, 83)
    lst = sorted([ord(char) for char in str_slice])
    return chr(lst[19])