def return_n_greatest_chars(str):
    str = sorted([ch for ch in str], key=ord, reverse=True)[:66]
    return str