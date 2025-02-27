def return_n_greatest_chars(s):
    if len(s) <= 47:
        return sorted(s)
    return sorted(sorted(s, reverse=True)[:47])