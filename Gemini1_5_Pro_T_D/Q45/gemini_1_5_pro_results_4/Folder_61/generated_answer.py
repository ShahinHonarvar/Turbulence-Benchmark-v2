from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 8) if string[i].isalpha()))
    palindromes = set()
    for i in range(7, len(string) + 1):
        for candidate_tuple in permutations(letters.elements(), i):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1] and len(candidate) >= 7:
                palindromes.add(candidate)
    return palindromes