def filter_chars(s):
    result = ''
    for char in s:
        if (char > 'Y' and char < 's') and 3 <= s.index(char) <= 5:
            continue
        else:
            result += char
    return result