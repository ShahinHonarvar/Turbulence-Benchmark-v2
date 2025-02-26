def return_n_greatest_chars(string):
    sorted_chars = sorted(set(string), reverse=True)
    return sorted_chars[:87] if len(sorted_chars) >= 87 else sorted_chars