from itertools import combinations_with_replacement

def all_substring_of_size_n(string):
    all_combinations = []
    for i in range(len(string) + 1):
        for j in range(i):
            for combination in combinations_with_replacement(range(j, i), 98):
                if len(set(combination)) == 98:
                    all_combinations.append(''.join([string[i] for i in combination]))
    return all_combinations