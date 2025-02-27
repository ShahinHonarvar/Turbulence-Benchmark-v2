from itertools import product

def all_substring_of_size_n(string):
    all_substrings = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 32 and len(set(substring)) == len(substring):
                all_substrings.add(substring)
    return list(all_substrings)