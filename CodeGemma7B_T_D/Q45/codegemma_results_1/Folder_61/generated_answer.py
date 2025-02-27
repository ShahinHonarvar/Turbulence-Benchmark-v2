from itertools import permutations

def palindromes_between_indices(text):
    palindromes = set()
    for position in range(len(text) - 6):
        substring = text[position:position + 7]
        if substring.lower() == substring.lower()[::-1]:
            for permutation in permutations(substring):
                palindromes.add(''.join(permutation))
    return palindromes