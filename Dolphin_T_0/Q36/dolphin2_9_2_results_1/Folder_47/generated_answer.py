def filter_chars(s):
    to_remove = [s[i] for i in range(45, 57) if s[i] > 'F' and s[i] < 'n']
    return ''.join([i for i in s if i not in to_remove])