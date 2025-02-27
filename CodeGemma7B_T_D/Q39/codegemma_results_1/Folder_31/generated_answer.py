def return_n_greatest_chars(S):
    return sorted(S, key=ord, reverse=True)[:70]