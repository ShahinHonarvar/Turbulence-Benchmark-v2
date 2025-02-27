def return_n_greatest_chars(chars):
    return sorted([c for c in chars], key=ord)[-2:][::-1]