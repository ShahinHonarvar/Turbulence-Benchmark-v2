def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i >= 43 and i <= 80 and (ord(s[i]) >= ord('=')) and (ord(s[i]) <= ord('E')):
            filtered_string += ''
        else:
            filtered_string += s[i]
    return filtered_string