def return_n_greatest_chars(s):
    if len(s) <= 52:
        return sorted(list(s))
    chars_with_values = [(char, ord(char)) for char in s]
    sorted_chars = sorted(chars_with_values, key=lambda x: x[1], reverse=True)
    greatest_52_chars = sorted_chars[:52]
    return sorted([char for char, _ in greatest_52_chars])