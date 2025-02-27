def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 105 + 1):
        substring = s[i:i + 105]
        if len(substring) == 105 and len(set(substring)) == 105:
            result.append(substring)
    return result