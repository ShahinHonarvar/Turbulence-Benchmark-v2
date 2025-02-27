def return_n_smallest_chars(s):
    ascii_chars = [ord(c) for c in s]
    ascii_chars.sort()
    sorted_chars = [chr(d) for d in ascii_chars[:38]]
    sorted_chars.sort(reverse=True)
    return sorted_chars