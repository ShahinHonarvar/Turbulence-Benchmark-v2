def return_n_greatest_chars(str):
    if len(str) != len(set(str)):
        return None
    return sorted([char for char in str], key=ord, reverse=True)[:39]