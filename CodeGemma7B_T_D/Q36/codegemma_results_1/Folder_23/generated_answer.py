def filter_chars(str):
    filtered_str = ''.join([c for c in str if c not in [str[i] for i in range(21, 25) if str[i] > '5' and str[i] < '}']])
    return filtered_str