def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 129):
        substring = s[i:i + 130]
        if len(set(substring)) == 130:
            result.append(substring)
    return result