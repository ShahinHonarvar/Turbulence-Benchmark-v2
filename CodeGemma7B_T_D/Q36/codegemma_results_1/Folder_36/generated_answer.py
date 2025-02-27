def filter_chars(s):
    filtered_str = []
    for i in range(len(s)):
        if i >= 283 and i <= 484 and (s[i] > 'l') and (s[i] < 't'):
            continue
        filtered_str.append(s[i])
    return ''.join(filtered_str)