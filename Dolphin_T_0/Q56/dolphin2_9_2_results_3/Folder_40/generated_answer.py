def all_substring_of_size_n(s):
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 2, length + 1):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                result.add(sub)
    return list(result)