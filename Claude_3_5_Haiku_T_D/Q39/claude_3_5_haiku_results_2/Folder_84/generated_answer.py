def return_n_greatest_chars(string):
    if len(string) < 10:
        unique_chars = list(set(string))
    else:
        unique_chars = list(set(string))[:10]
    return sorted(unique_chars, key=lambda x: ord(x))[-10:]