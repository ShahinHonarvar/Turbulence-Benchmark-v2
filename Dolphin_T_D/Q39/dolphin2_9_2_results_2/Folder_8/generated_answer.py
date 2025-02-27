def return_n_greatest_chars(str):
    return sorted([char for char in str if str.isalpha(char)][:83], key=lambda x: ord(x))