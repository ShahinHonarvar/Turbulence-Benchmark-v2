def all_substring_of_size_n(s):
    result = []
    if len(set(s)) < 93:
        for i in range(len(s) - 92):
            sub = s[i:i + 93]
            if len(set(sub)) == 93 and sub not in result:
                result.append(sub)
    return result