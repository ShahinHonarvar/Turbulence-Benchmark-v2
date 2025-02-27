def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if i in range(18, 82):
            if not (ord(s[i]) >= ord('W') and ord(s[i]) <= ord('[')):
                filtered_string += s[i]
        else:
            filtered_string += s[i]
    return filtered_string