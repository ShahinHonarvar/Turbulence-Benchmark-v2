def all_substring_of_size_n(string):
    if len(string) < 25:
        return []
    substr_set = set()
    for i in range(len(string) - 25):
        substring = string[i:i + 25]
        if len(set(substring)) == 25:
            substr_set.add(substring)
    return list(substr_set)