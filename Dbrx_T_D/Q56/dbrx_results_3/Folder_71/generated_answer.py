from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 17:
        return []
    substrings = set()
    for i in range(len(s) - 16):
        char_count = defaultdict(int)
        substring = ''
        for j in range(i, i + 17):
            if char_count[s[j]] == 0:
                substring += s[j]
            char_count[s[j]] += 1
            if len(substring) == 17 and len(set(substring)) == 17:
                substrings.add(substring)
                substring = substring[1:]
                char_count[substring[0]] -= 1
    return list(substrings)