from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[5:8] if c.isalpha()]
    counter = Counter((c.lower() for c in letters))
    palindromes = set()
    for r in range(2, len(letters) // 2 + 1):
        for combo in itertools.combinations_with_replacement(counter.elements(), r):
            palindrome = ''.join(combo) + ''.join(reversed(combo))
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes