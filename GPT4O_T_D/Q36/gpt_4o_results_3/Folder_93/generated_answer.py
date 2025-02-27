def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('&') + 1, ord('c'))}
    filtered_string = ''
    for i, char in enumerate(s):
        if i <= 52 or i >= 88 or char not in to_remove:
            filtered_string += char
    return filtered_string