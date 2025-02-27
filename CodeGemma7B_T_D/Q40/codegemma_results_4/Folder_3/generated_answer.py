def return_n_smallest_chars(chars):
    return sorted([ch for ch in chars], key=ord, reverse=True)[:28]