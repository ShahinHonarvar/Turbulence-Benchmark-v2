def filter_chars(s):
    filtered_chars = [char for char in s[42:68] if not 't' < char < 'x']
    return ''.join(s[:42] + filtered_chars + s[68:])