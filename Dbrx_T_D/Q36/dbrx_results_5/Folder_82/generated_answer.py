def filter_chars(s):
    filtered_chars = [char for char in s[69:97] if s.count(char) > 0 and (not 'V' < char < 'j')]
    return ''.join([char for char in s if char not in filtered_chars])