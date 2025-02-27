def filter_chars(string):
    new_str = []
    for i in range(len(string)):
        if i >= 164 and i <= 706 and (string[i] >= 'O') and (string[i] <= '}'):
            continue
        new_str.append(string[i])
    return ''.join(new_str)