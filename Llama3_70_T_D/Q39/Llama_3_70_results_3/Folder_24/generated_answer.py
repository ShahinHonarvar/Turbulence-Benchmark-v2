def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: (x.islower(), x), reverse=True)
    return sorted_chars[:32]