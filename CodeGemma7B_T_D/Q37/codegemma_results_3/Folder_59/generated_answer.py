def filter_chars(str):
    return ''.join([char for char in str if char not in string.ascii_uppercase and char not in string.ascii_lowercase and (5 <= ord(char) <= 95)])