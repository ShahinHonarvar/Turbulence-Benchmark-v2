def filter_chars(s):
    filtered_chars = []
    for i, char in enumerate(s):
        if 19 < i < 69 and '<' < char < 'C':
            s = s.replace(char, '')
    return s