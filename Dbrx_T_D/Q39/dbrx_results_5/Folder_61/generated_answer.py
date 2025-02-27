def return_n_greatest_chars(string):
    distinct_chars = list(set(string))
    distinct_chars.sort(key=lambda char: ord(char), reverse=True)
    return distinct_chars[:66]