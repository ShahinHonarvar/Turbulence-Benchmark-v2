def filter_chars(s):
    if len(s) <= 10:
        return s
    filtered_chars = {chr(i) for i in range(ord('?') + 1, ord('m'))}
    result = list(s)
    for i in range(11, min(79, len(s) - 1)):
        if s[i] in filtered_chars:
            result = [char for char in result if char != s[i]]
    return ''.join(result)