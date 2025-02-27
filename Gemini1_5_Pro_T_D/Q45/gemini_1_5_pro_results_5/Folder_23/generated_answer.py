from collections import Counter
  import itertools

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    relevant_string = ''.join((ch for ch in string[:7] if ch in letters))
    length = len(relevant_string)
    if length < 4:
        return set()
    character_counts = Counter(relevant_string)
    permutations = set()
    for i in range(4, length + 1):
        for combination in itertools.combinations_with_replacement(character_counts.keys(), i):
            if all((character_counts[ch] >= count for ch, count in Counter(combination).items())):
                for permutation in itertools.permutations(combination):
                    permutations.add(''.join(permutation))
    palindromes = {''.join(permutation) for permutation in permutations if ''.join(permutation) == ''.join(reversed(''.join(permutation)))}
    return palindromes