def return_n_greatest_chars(chars):
    return sorted([char for char in chars], key=ord, reverse=True)[:45]