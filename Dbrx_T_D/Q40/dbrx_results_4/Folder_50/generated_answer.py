def return_n_smallest_chars(string):
    distinct_chars = list(set(string))
    distinct_chars.sort(reverse=True)
    if len(distinct_chars) < 16:
        return distinct_chars
    else:
        return distinct_chars[:16]