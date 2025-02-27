def return_n_greatest_chars(string):
    sorted_chars = sorted([char for char in string], reverse=True)
    return sorted([char for char in sorted_chars][:29])