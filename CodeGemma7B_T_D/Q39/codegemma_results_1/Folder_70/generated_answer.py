def return_n_greatest_chars(str):
    top_two_chars = sorted(str, key=ord, reverse=True)[:2]
    return top_two_chars