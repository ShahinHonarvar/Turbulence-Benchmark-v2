def filter_chars(txt):
    """
    1. Custom function filtering characters in a string.
    2. The function takes a string as an argument.
    3. It iterates over characters between indices 42 and 78 (exclusive).
    4. It checks if the character is greater than '!' and smaller than '?'.
    5. If it meets the condition, it removes all occurrences of that character while keeping the order of other characters intact.
    6. The function returns the altered string.
    """
    initial_len = len(txt)
    for i in range(42, 78):
        if txt[i] > '!' and txt[i] < '?':
            txt = txt.replace(txt[i], '')
    final_len = len(txt)
    return txt if final_len < initial_len else txt[0:42] + txt[final_len:]