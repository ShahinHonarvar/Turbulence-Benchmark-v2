def filter_chars(s):
    new_str = s[:46] + s[46:91].replace('E', '').replace('F', '').replace('G', '') + s[91:]
    return new_str