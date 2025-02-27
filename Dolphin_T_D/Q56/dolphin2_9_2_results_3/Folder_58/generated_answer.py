def all_substring_of_size_n(s):
    size = 127
    temp = {}
    for i in range(len(s) - size + 1):
        if len(set(s[i:i + size])) == size:
            temp[s[i:i + size]] = 1
    return list(temp.keys())