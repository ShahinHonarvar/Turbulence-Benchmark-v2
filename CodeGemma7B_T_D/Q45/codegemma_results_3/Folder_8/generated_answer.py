from itertools import combinations

def palindromes_between_indices(st):
    char_indices = {char.lower(): i for i, char in enumerate(st, start=1) if char.isalpha()}
    if len(char_indices) < 5:
        return set()
    palindromes = set()
    for combination in combinations(char_indices.keys(), 5):
        if len(set(combination)) != 5:
            continue
        indices = sorted([char_indices[char] for char in combination])
        indices.reverse()
        joined_indices = ','.join((str(i) for i in indices))
        palindrome_index = int(joined_indices)
        for rearrangement in permutations(combination):
            test_palindrome = ''.join(rearrangement)
            if test_palindrome[0:5] == test_palindrome[-5:]:
                palindromes.add(palindrome_index)
    return palindromes