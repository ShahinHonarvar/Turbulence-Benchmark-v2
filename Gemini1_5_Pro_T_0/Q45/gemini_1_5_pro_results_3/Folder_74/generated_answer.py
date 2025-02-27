from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[1:7].lower())
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for candidate_tuple in permutations(letters, i):
            candidate = ''.join(candidate_tuple)
            if candidate == candidate[::-1] and len(candidate) >= 6:
                candidate_counter = Counter(candidate)
                if all((candidate_counter[letter] <= letters[letter] for letter in candidate_counter)):
                    palindromes.add(candidate)
    return palindromes