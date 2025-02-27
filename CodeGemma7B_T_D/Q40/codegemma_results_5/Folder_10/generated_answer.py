def return_n_smallest_chars(distinct_chars):
    unique_chars = sorted(distinct_chars)
    sorted_chars = sorted([ord(char) for char in unique_chars], reverse=True)
    return sorted_chars[:88]