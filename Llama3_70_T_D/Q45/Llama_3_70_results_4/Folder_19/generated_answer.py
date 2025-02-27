from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:8] if c.isalpha()]
    counter = Counter(letters)
    palindromes = set()
    for middle in letters:
        counter[middle] -= 1
        for p in permutations([c for c, n in counter.items() if n > 0], len(letters) - 1):
            palindrome = ''.join(p[:len(p) // 2]) + middle + ''.join(p[len(p) // 2:])
            if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
        counter[middle] += 1
    return palindromes