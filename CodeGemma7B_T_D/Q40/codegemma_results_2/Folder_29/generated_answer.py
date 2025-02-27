def return_n_smallest_chars(chars):
    return sorted([char for char in chars], key=ord, reverse=True)[:23]