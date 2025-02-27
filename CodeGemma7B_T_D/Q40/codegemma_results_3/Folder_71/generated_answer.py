def return_n_smallest_chars(chars: str) -> list:
    return sorted([i for i in chars], key=ord)[:14]