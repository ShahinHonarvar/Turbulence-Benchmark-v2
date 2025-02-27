def return_n_greatest_chars(s):
    ascii_chars = [ord(c) for c in s if ord(c) >= 32 and ord(c) <= 126]
    sorted_ascii = sorted(ascii_chars, reverse=True)[:52]
    return [chr(c) for c in sorted_ascii]