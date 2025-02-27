def all_substring_of_size_n(string):
    n = 73
    if len(string) < n:
        return []
    substrings = []
    seen = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
            seen.add(tuple(substring))
    return substrings