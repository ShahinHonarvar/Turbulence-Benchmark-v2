def return_n_greatest_chars(str):
    return sorted([char for char in str], reverse=True)[:11]