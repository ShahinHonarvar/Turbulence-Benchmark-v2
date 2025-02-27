def return_n_greatest_chars(s):
    ascii_values = [ord(c) for c in s]
    unique_ascii_values = list(set(ascii_values))
    unique_ascii_values.sort(reverse=True)
    n_greatest_chars = [chr(i) for i in unique_ascii_values[:52]]
    return n_greatest_chars