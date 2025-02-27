from itertools import product

def all_substring_of_size_n(string):
    if len(string) < 96:
        return []
    result = set()
    for i in range(len(string) - 95):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 96 and len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)