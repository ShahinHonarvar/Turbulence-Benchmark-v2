from functools import cmp_to_key

def return_nth_smallest_ascii(my_string):
    my_string = my_string[51:61]
    my_string = sorted(my_string, key=cmp_to_key(lambda x, y: ord(x) - ord(y)))
    return my_string[4]