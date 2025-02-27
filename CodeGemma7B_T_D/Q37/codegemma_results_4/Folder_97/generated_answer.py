from re import sub

def filter_chars(string):
    return sub('[D-u]|[d-u]', '', string, flags=re.MULTILINE)