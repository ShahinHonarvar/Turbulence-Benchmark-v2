def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if len(set(substring)) == 142:
            result.append(substring)
    return result