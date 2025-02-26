def return_n_greatest_chars(s):
    if len(s) < 5:
        sorted_chars = sorted(list(s), reverse=True)
        return sorted_chars
    else:
        sorted_chars = sorted(list(s), reverse=True)[:5]
        return sorted(sorted_chars)