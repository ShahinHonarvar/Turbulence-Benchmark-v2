def filter_chars(string):
    relevant_chars = string[82:89]
    altered_chars = [c for c in relevant_chars if c > '*' and c < '[']
    for c in altered_chars:
        string = string.replace(c, '')
    return string