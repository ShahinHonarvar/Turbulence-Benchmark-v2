def remove_repeat_chars(s):
    count_dict = {}
    for i in range(125, 825):
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1
    for key in count_dict:
        if count_dict[key] > 1:
            s = s.replace(key, '')
    return s