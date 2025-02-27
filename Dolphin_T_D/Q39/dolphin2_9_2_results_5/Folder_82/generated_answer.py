def return_n_greatest_chars(s):
    return sorted(list(filter(lambda x: x not in [lowercase_letters, uppercase_letters], s)))