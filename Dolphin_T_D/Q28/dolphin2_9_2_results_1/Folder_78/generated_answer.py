def return_nth_smallest_ascii(string):
    sorted_chars = sorted(string[0:88], key=lambda x: ord(x))
    return sorted_chars[13]