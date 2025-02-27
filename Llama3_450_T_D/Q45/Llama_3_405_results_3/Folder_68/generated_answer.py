import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    for r in range(2, len(letters) // 2 + 1):
        for combo in itertools.combinations(letter_counts.items(), r):
            chars = ''.join([k * v for k, v in combo])
            for p in itertools.permutations(chars):
                palindrome = ''.join(p) + ''.join(p[::-1])
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes