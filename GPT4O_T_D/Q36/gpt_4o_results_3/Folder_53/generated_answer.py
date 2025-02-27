def filter_chars(s):
    to_remove = set()
    substring = s[91:97]
    for char in substring:
        if 'j' < char < 'w':
            to_remove.add(char)
    result = ''.join((char for char in s if char not in to_remove))
    return result