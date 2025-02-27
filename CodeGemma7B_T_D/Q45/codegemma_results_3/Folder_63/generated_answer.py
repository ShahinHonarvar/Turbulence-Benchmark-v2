from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    letter_counts = defaultdict(int)
    for char in s[0:4]:
        letter_counts[char.lower()] += 1

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]
    palindromes = set()
    for permutation in itertools.permutations(letter_counts.keys()):
        candidate = ''.join(permutation)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes