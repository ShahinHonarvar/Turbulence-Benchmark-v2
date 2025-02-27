from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(6) if string[i].isalpha()])
    palindromes = set()
    for length in range(6, len(string) + 1):
        for candidate in permutations(letters.elements(), length):
            candidate_string = ''.join(candidate)
            if candidate_string == candidate_string[::-1]:
                palindromes.add(candidate_string)
    return palindromes