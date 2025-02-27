def return_n_greatest_chars(chars):
    ascii_values = sorted([ord(c) for c in chars], reverse=True)[:66]
    return [chr(c) for c in ascii_values]