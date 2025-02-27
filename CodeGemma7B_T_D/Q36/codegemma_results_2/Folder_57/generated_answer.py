def filter_chars(s):
    filtered_string = ''
    for i in range(len(s)):
        if s[i] in [chr(j) for j in range(ord('A') + 70, ord('A') + 74)]:
            continue
        filtered_string += s[i]
    return filtered_string