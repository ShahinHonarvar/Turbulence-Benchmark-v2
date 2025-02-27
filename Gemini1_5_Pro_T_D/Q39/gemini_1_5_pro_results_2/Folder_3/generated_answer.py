def return_n_greatest_chars(text: str):
    return sorted([*text], reverse=True)[:28]