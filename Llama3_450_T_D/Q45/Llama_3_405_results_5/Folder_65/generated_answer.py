from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    letters = ''.join((letter * counter[letter] for letter in counter))
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes