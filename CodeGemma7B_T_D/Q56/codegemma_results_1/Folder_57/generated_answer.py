def all_substring_of_size_n(s):
    """Return all distinct substrings of length n from a string with no duplicate characters"""
    map_seen = dict()
    output = []
    for i in range(len(s) - 59):
        substring = s[i:i + 60]
        if substring not in map_seen:
            map_seen[substring] = 0
            output.append(substring)
    return output