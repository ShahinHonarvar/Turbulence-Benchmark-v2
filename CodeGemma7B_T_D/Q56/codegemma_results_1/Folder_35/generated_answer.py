def all_substring_of_size_n(s):
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if len(set(substring)) == len(substring):
            return [substring]
    return []