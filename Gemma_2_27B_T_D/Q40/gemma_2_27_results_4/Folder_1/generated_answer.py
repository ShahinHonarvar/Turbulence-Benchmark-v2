def return_n_smallest_chars(chars):
    return sorted([c for c in chars], reverse=True)[:11]