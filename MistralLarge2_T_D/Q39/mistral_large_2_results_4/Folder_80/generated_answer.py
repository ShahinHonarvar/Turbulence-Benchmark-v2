def return_n_greatest_chars(s):
    return sorted([char for char in s if len(set(s)) >= 35], key=ord, reverse=True)[:35]