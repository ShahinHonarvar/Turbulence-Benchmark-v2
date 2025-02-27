from collections import Counter
    from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(8) if string[i].isalpha()))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for candidate_tuple in permutations(letters.elements(), length):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes