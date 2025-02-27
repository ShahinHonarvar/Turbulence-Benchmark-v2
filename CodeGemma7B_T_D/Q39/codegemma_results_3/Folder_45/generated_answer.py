from string import ascii_uppercase, ascii_lowercase

def return_n_greatest_chars(str):
    if not isinstance(str, str) or not str:
        return None
    if len(str) > 52:
        str = str[:52]
    return sorted(str, reverse=True)