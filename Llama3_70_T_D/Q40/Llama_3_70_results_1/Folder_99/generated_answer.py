def return_n_smallest_chars(s):
    return sorted([min(s, key=ord) for _ in range(35)], reverse=True)