def return_n_greatest_chars(string):
    return sorted(list(set(string))[-54:], reverse=True)