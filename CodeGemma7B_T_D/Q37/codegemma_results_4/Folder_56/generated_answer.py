def filter_chars(some_str):
    filtered_str = ''
    for char in some_str:
        if not (71 <= ord(char) <= 94 and ord(char) >= ord('K') and (ord(char) <= ord('a'))):
            filtered_str += char
    return filtered_str