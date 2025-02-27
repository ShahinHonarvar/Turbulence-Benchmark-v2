def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 146 + 1):
        substring = s[i:i + 146]
        if len(set(substring)) == len(substring) and len(set(substring)) == 146:
            result.append(substring)
    return result