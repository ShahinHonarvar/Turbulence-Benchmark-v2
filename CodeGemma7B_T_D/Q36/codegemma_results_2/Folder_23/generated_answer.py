def filter_chars(s):
    new_list = []
    for i in range(len(s)):
        if i < 21 or i > 25:
            new_list.append(s[i])
    return ''.join(new_list)