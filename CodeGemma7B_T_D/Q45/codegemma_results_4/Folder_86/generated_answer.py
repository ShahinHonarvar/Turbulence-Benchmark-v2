from itertools import permutations
    from collections import defaultdict

def palindromes_between_indices(text):
    letter_counts = defaultdict(int)
    for char in text[6:10]:
        if char.isalpha():
            letter_counts[char.lower()] += 1
    palindromes = set()
    for perm in permutations('abcdefghijklmnopqrstuvwxyz', r=len(letter_counts)):
        if ''.join(perm[:len(letter_counts)]) in letter_counts:
            palindromes.add(''.join(perm))
    return palindromes