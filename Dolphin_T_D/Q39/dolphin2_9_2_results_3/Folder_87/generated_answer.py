def return_n_greatest_chars(s):
    return sorted([ch for ch in s if ch.isalpha()], reverse=True)[:24]