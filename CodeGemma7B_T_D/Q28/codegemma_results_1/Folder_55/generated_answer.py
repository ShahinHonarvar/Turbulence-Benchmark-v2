def return_nth_smallest_ascii(chars):
    target_indices = range(13)
    return min((chars[i] for i in target_indices))