from itertools import permutations

def all_substring_of_size_n(s):
    if len(s) < 87:
        return []
    substrings = set()
    for i in range(len(s) - 86):
        for perm in permutations(s[i:i + 87]):
            substr = ''.join(perm)
            if len(substrings) >= 87:
                break
            if not any((c in substr for c in substrings)):
                substrings.add(substr)
    return list(substrings)