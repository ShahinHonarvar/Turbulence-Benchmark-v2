def return_n_greatest_chars(str):
    lst = sorted(str, key=lambda char: ord(char), reverse=True)[:32]
    return lst