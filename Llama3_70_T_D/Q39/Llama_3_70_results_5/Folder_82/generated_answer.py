def return_n_greatest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii = sorted(ascii_values, reverse=True)[:60]
    return [chr(i) for i in sorted(sorted_ascii)]