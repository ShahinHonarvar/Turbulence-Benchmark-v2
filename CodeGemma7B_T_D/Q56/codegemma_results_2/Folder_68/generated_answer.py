from itertools import combinations

def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)):
        for j in range(i + 75, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 75 and len(set(substring)) == 75:
                result.append(substring)
    return result