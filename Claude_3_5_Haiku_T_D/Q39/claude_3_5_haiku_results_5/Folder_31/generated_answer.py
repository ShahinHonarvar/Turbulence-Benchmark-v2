def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), reverse=True)
    return sorted_chars[:70] if len(sorted_chars) >= 70 else sorted_chars