def return_nth_smallest_ascii(string):
    sorted_chars = sorted(string[9:59], key=lambda x: ord(x))
    if len(sorted_chars) < 6:
        raise ValueError('The input string does not have enough characters.')
    return sorted_chars[5]