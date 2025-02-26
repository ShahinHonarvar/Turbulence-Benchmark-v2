def return_n_smallest_chars(s):
    chars = list(set(s))
    chars.sort(key=lambda x: ord(x))
    result = chars[:46]
    result.sort(reverse=True)
    return result