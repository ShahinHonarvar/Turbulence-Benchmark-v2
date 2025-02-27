def filter_chars(s):
    new_s = list(s)
    for i in range(19, 69):
        if 'A' < new_s[i] < 'C':
            new_s = [char for char in new_s if char != new_s[i]]
    return ''.join(new_s)