def filter_chars(s):
    filtered_str = ''
    for char in s:
        if not (char > '3' and char < 'D' and (32 < ord(char) < 61)):
            filtered_str += char
    return filtered_str