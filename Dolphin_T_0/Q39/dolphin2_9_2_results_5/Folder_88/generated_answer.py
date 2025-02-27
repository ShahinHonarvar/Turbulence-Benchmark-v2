def return_n_greatest_chars(s):
    return sorted([c for c in s if c in string.ascii_letters or c in string.punctuation], reverse=True, key=lambda x: string.ascii_letters.index(x))[:84]