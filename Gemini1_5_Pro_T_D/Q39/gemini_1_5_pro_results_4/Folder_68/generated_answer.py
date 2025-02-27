def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= sorted(list(set(text)), key=ord)[-89]], reverse=True)