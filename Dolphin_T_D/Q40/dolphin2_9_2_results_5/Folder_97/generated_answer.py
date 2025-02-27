def return_n_smallest_chars(s):
    ascii_s = [ord(c) for c in s]
    ascii_s.sort()
    return [chr(i) for i in ascii_s[:38]]