def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) >= sorted(list(set([ord(c) for c in text])))[-66]], reverse=True)