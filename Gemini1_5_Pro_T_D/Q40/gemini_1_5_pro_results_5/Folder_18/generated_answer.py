def return_n_smallest_chars(s):
    return sorted([c for c in s if ord(c) >= 32 and ord(c) <= 126][:52], reverse=True)