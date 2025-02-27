def return_n_greatest_chars(s):
    greatest_chars = filter(lambda x: x in s, map(chr, range(1, 128)))
    sorted_chars = sorted(greatest_chars)
    if len(sorted_chars) < 66:
        return sorted_chars
    else:
        return sorted_chars[-66:]