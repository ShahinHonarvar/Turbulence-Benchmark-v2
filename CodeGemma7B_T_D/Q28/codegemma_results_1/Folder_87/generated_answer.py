def return_nth_smallest_ascii(my_str):
    return min([x for x in my_str[29:34] if ord(x) > ord('e')], key=ord)