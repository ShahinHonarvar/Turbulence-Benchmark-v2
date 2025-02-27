def filter_chars(string):
    return string[:8] + ''.join([ch for ch in string[8:9] if ch < 'R' or ch > 't']) + string[9:]