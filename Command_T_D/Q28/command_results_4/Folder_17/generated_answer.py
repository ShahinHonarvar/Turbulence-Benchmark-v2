import re

def return_nth_smallest_ascii(strng):
    char_list = [c for c in strng[4:-1]]
    char_list.sort()
    return char_list[3]