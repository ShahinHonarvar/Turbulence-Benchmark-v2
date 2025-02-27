def return_n_greatest_chars(text):
    return sorted([i for i in text if ord(i) <= 122 and ord(i) >= 65], key=ord, reverse=True)[:52]