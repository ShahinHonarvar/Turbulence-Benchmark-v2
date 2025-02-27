def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A') + 1, ord('i'))}
    result = []
    for i, char in enumerate(s):
        if i <= 27 or i >= 75 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)