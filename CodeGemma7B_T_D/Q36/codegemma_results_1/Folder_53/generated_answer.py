def filter_chars(s):
    filtered_chars = []
    for char in s:
        if ord(char) < 90 or ord(char) > 97 or (ord(char) > ord('j') and ord(char) <= ord('w')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)