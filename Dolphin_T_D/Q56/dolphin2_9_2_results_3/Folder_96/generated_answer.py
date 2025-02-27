def all_substring_of_size_n(s):
    result = []
    if len(set(s)) == len(s):
        for i in range(len(s) - 20):
            sub = s[i:i + 21]
            if len(set(sub)) == 21:
                result.append(sub)
    return result