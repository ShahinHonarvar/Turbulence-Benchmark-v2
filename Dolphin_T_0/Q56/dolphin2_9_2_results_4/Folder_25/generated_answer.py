def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 66):
        found = set()
        for j in range(i, i + 67):
            if s[j] in found:
                break
            found.add(s[j])
        else:
            result.append(s[i:i + 67])
    return result