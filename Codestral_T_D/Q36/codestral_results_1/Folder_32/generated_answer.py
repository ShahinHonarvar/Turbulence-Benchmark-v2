def filter_chars(string):
    substring = string[40:63]
    filtered_substring = ''.join([c for c in substring if not '7' < c < 'H'])
    return string[:40] + filtered_substring + string[63:]