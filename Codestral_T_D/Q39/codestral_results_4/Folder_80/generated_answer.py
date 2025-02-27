def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)[:35]
    sorted_chars.sort()
    return sorted_chars