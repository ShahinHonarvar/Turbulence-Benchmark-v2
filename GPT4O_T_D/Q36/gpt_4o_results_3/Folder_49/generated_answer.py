def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('E'), ord('H'))}
    result = []
    for idx, char in enumerate(s):
        if idx <= 46 or idx >= 91 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)