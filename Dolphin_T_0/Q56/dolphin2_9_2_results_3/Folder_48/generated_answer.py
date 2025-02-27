def all_substring_of_size_n(s):
    result = set()
    length = len(s)
    for i in range(length - 119):
        sub = s[i:i + 120]
        if len(set(sub)) == len(sub):
            result.add(sub)
    return list(result)