def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    elif len(s) < 85:
        return []
    else:
        substrings = []
        for i in range(len(s) - 84):
            if len(set(s[i:i + 85])) == 85:
                substrings.append(s[i:i + 85])
        return substrings