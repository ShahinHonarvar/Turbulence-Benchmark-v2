def filter_chars(s):
    result = ''
    for char in s:
        if 36 <= ord(char) <= 40 and 'H' <= char <= 'e' or (36 > ord(char) or (ord(char) > 40 and 'H' > char) or char > 'e'):
            result = result + char
    return result