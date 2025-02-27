from collections import Counter
    from itertools import permutations

def palindromes_between_indices(text):
    letters = Counter((c.lower() for i, c in enumerate(text) if 1 <= i <= 6 and c.isalpha()))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for candidate in permutations(letters.elements(), length):
            word = ''.join(candidate)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes