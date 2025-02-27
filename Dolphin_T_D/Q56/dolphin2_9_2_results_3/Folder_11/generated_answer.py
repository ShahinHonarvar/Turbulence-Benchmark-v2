def all_substring_of_size_n(s):
    length = len(s)
    if length < 78:
        return []
    sub_strings = []
    for i in range(length - 77):
        sub = s[i:i + 78]
        if len(set(sub)) == len(sub):
            sub_strings.append(sub)
    return sub_strings