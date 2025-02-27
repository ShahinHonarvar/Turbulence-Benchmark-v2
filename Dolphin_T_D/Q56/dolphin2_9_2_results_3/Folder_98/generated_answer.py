def all_substring_of_size_n(string):
    if len(string) < 10:
        return []
    substrings = set()
    for i in range(len(string) - 9):
        substring = string[i:i + 10]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)