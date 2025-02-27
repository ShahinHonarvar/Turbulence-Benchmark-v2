from itertools import permutations

def all_substrings_of_size_n(string):
    result = []
    for i in range(len(string) - 87 + 1):
        substring = string[i:i + 87]
        if len(substring) == 87 and len(set(substring)) == 87:
            result.append(substring)
    return list(set(result))