from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:8].lower()))
    counter = Counter(s)
    letters = ''.join(counter.elements())
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes