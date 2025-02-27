def return_n_greatest_chars(text):
    return sorted([char for char in text if ord(char) in sorted([ord(c) for c in text], reverse=True)[:49]], reverse=True)