def return_n_greatest_chars(s):
    chars = []
    for char in s:
        chars.append(char)
    chars.sort(reverse=True)
    return chars[:28]