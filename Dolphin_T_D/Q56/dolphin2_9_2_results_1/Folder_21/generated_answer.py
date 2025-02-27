def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) == len(s[i:j]) and len(s[i:j]) == 106:
                result.append(s[i:j])
    return result