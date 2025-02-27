def filter_chars(s):
    filtered_chars = [char for char in s[11:46] if '!' < char < 'A']
    return s[:11] + ''.join(filtered_chars) + s[46:]