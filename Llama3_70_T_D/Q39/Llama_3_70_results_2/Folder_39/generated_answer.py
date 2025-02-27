def return_n_greatest_chars(s):
    return sorted([char for char in s if ord(char) >= ord(max(s)) - 23], reverse=False)