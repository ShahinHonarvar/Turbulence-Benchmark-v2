def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: x[-1] if isinstance(x, tuple) else x, reverse=True)[:16]