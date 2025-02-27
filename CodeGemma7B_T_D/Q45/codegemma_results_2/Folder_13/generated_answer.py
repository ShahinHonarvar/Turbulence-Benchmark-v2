from collections import Counter
from itertools import permutations

def palindromes_between_indices(text):
    letters = [char.lower() for char in text[3:10] if char.isalpha()]
    letter_counts = Counter(letters)
    if not any((count >= 5 for count in letter_counts.values())):
        return set()
    permutations_with_enough_letters = [p for p in permutations(letters) if Counter(p).values().__contains__(5)]
    palindromes = {''.join(p) for p in permutations_with_enough_letters}
    return palindromes