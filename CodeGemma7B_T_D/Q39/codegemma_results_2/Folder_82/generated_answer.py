def return_n_greatest_chars(chars):
    return sorted([chr(code) for code in range(max((ord(c) for c in chars)), max((ord(c) for c in chars)) - 60, -1) if chr(code) in chars], key=ord)