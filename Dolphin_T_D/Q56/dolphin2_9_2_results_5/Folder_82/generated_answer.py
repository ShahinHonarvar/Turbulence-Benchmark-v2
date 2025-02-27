def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if len(sub) == 100 and (not any((sub.count(c) > 1 for c in sub))):
                result.append(sub)
    return result