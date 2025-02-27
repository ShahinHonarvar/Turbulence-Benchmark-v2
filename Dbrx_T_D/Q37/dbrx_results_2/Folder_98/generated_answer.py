def filter_chars(s: str) -> str:
    i, j, k = (8, 9, 0)
    filtered_chars = [''] * len(s)
    filtered_length = 0
    while k < len(s):
        if i <= k <= j and s[k] >= 'R' and (s[k] <= 't'):
            k += 1
            continue
        else:
            filtered_chars[filtered_length] = s[k]
            filtered_length += 1
        k += 1
    return ''.join(filtered_chars[:filtered_length])