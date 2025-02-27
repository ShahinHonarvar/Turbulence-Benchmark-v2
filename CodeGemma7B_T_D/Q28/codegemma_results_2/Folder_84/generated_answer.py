def return_nth_smallest_ascii(string):
    return min([ord(c) for c in string[52:80] if ord(c) >= ord('a')], key=ord)