def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(set(substring)) == 99:
            result.append(substring)
    return result