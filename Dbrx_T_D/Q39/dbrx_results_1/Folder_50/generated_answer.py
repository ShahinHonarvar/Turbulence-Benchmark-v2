def return_n_greatest_chars(s):
    if len(s) < 16:
        return sorted(s, key=ord, reverse=True)
    else:
        return sorted(s, key=ord, reverse=True)[:16]