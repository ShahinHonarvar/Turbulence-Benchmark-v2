def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 91, len(s) + 1):
            sub = s[i:j]
            if len(sub) == 91 and len(set(sub)) == 91:
                result.append(sub)
    return list(set(result))