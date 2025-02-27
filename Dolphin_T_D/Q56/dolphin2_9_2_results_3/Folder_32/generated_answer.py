def all_substring_of_size_n(s):
    length_s = len(s)
    list_substring = []
    for i in range(0, length_s - 69):
        sub = s[i:i + 70]
        sub_set = set(sub)
        if len(sub_set) == len(sub):
            list_substring.append(sub)
    return list(set(list_substring))