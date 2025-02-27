from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    count = Counter(s[1:8])
    letters = ''
    for char, freq in count.items():
        if char.isalpha():
            letters += char * freq
    palindromes = set()
    for perm in permutations(letters, 5):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes