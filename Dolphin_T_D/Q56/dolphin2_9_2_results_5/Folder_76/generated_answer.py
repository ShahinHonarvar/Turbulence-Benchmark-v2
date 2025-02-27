def all_substring_of_size_n(string):
    if len(string) < 149:
        return []
    results = []
    for i in range(len(string) - 148):
        substring = string[i:i + 149]
        if len(set(substring)) == len(substring):
            results.append(substring)
    return results