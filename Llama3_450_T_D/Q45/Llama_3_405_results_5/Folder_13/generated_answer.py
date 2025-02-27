from itertools import combinations, permutations

def palindromes_between_indices(s):
    s = s[3:10].lower()
    english_letters = [c for c in s if 'a' <= c <= 'z']
    if len(english_letters) < 5:
        return set()
    palindromes = set()
    for r in range(5, len(english_letters) + 1):
        for c in combinations(english_letters, r):
            for p in permutations(c):
                palindrome = ''.join(p)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes