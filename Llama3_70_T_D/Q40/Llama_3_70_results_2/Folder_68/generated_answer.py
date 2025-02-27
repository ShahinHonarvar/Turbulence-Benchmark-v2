def return_n_smallest_chars(s):
    if len(s) < 89:
        return sorted(s, reverse=True)
    else:
        return sorted(s[:89], reverse=True)