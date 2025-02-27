from itertools import permutations

def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 7):
        for perm in permutations(string[i:i + 8]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)