def all_substring_of_size_n(s):
    output = []
    size = 74
    for i in range(len(s) - size + 1):
        substring = s[i:i + size]
        if len(set(substring)) == len(substring):
            output.append(substring)
    return list(set(output))