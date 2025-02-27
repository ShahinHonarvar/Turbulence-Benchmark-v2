def return_n_greatest_chars(text):
    return sorted(text, key=lambda c: ord(c), reverse=True)[:37]