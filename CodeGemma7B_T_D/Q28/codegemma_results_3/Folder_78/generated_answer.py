def return_nth_smallest_ascii(str):
    return max([c for c in str[0:88] if ord(c) >= ord('a')], key=ord)