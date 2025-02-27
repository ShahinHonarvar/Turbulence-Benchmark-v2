def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 7):
        temp = s[i:i + 8]
        if len(set(temp)) == 8 and temp not in result:
            result.append(temp)
    return result