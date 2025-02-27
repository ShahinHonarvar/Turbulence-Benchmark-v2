def filter_chars(s):
    filtered_chars = [char for char in s if not (s.index(char) > 43 and s.index(char) < 59 and ('5' < char < 'C'))]
    return ''.join(filtered_chars)