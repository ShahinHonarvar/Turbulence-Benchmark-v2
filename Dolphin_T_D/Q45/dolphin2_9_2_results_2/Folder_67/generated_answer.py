from itertools import permutations

def palindromes_between_indices(S):
    letters = ''.join((ch for ch in S[2:7] if ch.isalpha()))
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes