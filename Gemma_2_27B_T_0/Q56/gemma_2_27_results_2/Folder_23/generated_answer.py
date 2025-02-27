def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if len(set(substring)) == 42:
            result.append(substring)
    return result