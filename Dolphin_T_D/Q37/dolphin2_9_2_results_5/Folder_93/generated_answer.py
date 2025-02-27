def filter_chars(s):
    filtered_s = ''
    for char in s:
        if 38 <= s.index(char) <= 69 and 'H' <= char <= 'e':
            filtered_s += s.replace(char, '')
        else:
            filtered_s += char
    return filtered_s