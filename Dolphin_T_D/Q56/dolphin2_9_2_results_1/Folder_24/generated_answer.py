def all_substring_of_size_n(s):
    length = len(s)
    result = []
    i = 0
    while i + 52 <= length:
        substring = s[i:i + 52]
        if len(set(substring)) == len(substring):
            result.append(substring)
        i += 1
    return result