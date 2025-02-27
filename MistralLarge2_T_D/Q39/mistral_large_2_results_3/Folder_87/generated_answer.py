def return_n_greatest_chars(s):
    return sorted([char for char in s if ord(char) in range(256)], key=ord, reverse=True)[:24][::-1]