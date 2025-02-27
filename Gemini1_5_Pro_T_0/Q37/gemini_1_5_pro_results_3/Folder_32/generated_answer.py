def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 23 and i <= 89 and (ord(s[i]) >= ord('w')) and (ord(s[i]) <= ord('{')):
            continue
        else:
            filtered_string += s[i]
    return filtered_string