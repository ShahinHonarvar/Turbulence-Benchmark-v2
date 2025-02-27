def all_substring_of_size_n(s):
    if len(set(s)) == 1 and len(s) == 1:
        return []
    length = len(s)
    result = []
    for i in range(length):
        for j in range(i + 67, length + 1):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                result.append(sub)
    return list(set(result))