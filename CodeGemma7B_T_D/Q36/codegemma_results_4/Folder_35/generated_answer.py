def filter_chars(t):
    output = ''
    for i in range(len(t)):
        if i >= 163 and i < 658 and (t[i] > '(') and (t[i] < ']'):
            continue
        output += t[i]
    return output