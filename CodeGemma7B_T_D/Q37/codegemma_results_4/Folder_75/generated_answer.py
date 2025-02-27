def filter_chars(s):
    output = []
    for i in range(len(s)):
        if i >= 34 and i <= 67 and (ord(s[i]) >= ord('W')) and (ord(s[i]) <= ord('x')):
            continue
        output.append(s[i])
    return ''.join(output)