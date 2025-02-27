def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: c.zfill(1), reverse=True)[:88]