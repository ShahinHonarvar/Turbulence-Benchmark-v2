import itertools

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    english_letters = [c.lower() for c in s[4:6] if c.isalpha()]
    palindrome_set = set()
    for length in range(3, 7):
        for combo in itertools.permutations(english_letters, length):
            if combo == combo[::-1]:
                palindrome_set.add(''.join(combo))
    return palindrome_set