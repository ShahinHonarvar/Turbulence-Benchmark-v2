from itertools import product
from collections import defaultdict

def palindrome_of_length_n(s):
    result = set()
    occurrences = defaultdict(int)
    for char in s.lower():
        occurrences[char] += 1
    for length in range(1, len(s) + 1):
        if 210 % length == 0:
            add_palindromes(result, occurrences, length)
    return result

def add_palindromes(result, occurrences, length):
    half_length = length // 2
    characters = set(occurrences.keys())
    for pattern in product(characters, repeat=half_length):
        palindrome = ''.join(pattern * 2)
        if has_sufficient_characters(occurrences, pattern):
            result.add(palindrome)

def has_sufficient_characters(occurrences, pattern):
    character_counts = defaultdict(int)
    for char in pattern:
        character_counts[char] += 1
    for char, count in character_counts.items():
        if occurrences[char] < count:
            return False
    return True