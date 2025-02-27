def return_n_greatest_chars(s):
    return sorted([ch for ch in s if ch in string.ascii_letters or ch in string.digits], reverse=True)[:64]