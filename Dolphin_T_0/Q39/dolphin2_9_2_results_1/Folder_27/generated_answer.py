def return_n_greatest_chars(s):
    chars = [char for char in s if ord(char) >= 32 and ord(char) < 127]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[-82:]