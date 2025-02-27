import functools

def return_nth_smallest_ascii(str):
    sorted_chars = sorted(str[47:81], key=functools.cmp_to_key(ord))
    return sorted_chars[3]