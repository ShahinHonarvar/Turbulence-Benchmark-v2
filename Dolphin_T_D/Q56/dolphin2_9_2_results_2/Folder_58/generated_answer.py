def all_substring_of_size_n(string):
    if len(string) < 127:
        return []
    substrings = set()
    for i in range(0, len(string) - 127 + 1):
        substrings.add(string[i:i + 127])
    return [s for s in substrings if len(set(s)) == len(s) == 127]