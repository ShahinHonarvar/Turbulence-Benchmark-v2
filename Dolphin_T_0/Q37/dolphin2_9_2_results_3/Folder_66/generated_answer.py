def filter_chars(s):
    alter = list(s)
    for i in range(27, 86):
        if alter[i] >= 'c' and alter[i] <= 'i':
            alter = [ch for ch in alter if ch != alter[i]]
    return ''.join(alter)