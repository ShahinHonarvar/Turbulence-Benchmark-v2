def all_substring_of_size_n(s):
    length = 50
    strings = []
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            strings.append(substring)
    return list(set(strings))