def return_n_greatest_chars(s):
    return sorted([char for char in s if ord(char) >= 128 and len([c for c in s if ord(c) < ord(char)]) < 83], reverse=False)