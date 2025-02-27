def return_n_greatest_chars(s):
    ascii_sorted = sorted((ord(c) for c in s))
    n_greatest_ascii = ascii_sorted[-37:]
    n_greatest_chars = [chr(i) for i in n_greatest_ascii]
    return sorted(n_greatest_chars)