def return_n_greatest_chars(s):
    chars = [char for char in s if char.isalnum()]
    chars.sort(reverse=True, key=lambda c: ord(c))
    return chars[:40]