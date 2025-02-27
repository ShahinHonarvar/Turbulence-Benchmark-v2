from itertools import filterfalse

def return_nth_smallest_ascii(test_string):
    ascii_list = [ord(char) for char in test_string]
    filtered_list = filterfalse(lambda x: x > ord('Z') or x < ord('a'), ascii_list)
    return sorted(filtered_list)[9]