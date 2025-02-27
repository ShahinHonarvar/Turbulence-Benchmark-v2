from collections import defaultdict
from itertools import combinations

def palindromes_between_indices(string):
    letters = defaultdict(list)
    for i, char in enumerate(string[1:3], 1):
        letters[char.lower()].append(i)
    palindromes = set()
    for length in range(3, len(string) + 1):
        for indices in combinations(letters.values(), length):
            mid = (indices[-1] + indices[0]) // 2
            if indices[0] == indices[-1]:
                palindromes.add(string[indices[0]:mid + 1] + string[mid:].lower())
            else:
                palindromes.add(string[indices[0]:mid] + string[mid:mid + 1] + string[mid + 1:].lower())
    return palindromes