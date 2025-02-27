def filter_chars(string):
    if len(string) <= 99:
        return string
    return ''.join([i for i in string[:75] + [i for i in string[100:]] if i not in string[75:100]])