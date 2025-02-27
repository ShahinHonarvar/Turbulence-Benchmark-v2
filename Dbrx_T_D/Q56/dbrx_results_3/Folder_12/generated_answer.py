def all_substring_of_size_n(s):
    if len(s) < 47 or len(set(s)) < 47:
        return []
    else:
        result = []
        for i in range(len(s) - 47 + 1):
            substring = s[i:i + 47]
            if len(set(substring)) == 47:
                result.append(substring)
        return list(set(result))