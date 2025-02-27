def return_n_greatest_chars(s):
    ascii_values = [ord(c) for c in s]
    sorted_ascii_values = sorted(ascii_values)[-76:]
    return [chr(n) for n in sorted_ascii_values]