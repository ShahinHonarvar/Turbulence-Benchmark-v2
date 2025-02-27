def return_n_greatest_chars(s):
    return sorted([char for char in s if ord(char) in sorted(set([ord(char) for char in s]), reverse=True)[:29]])