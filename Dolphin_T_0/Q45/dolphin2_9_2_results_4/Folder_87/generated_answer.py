from itertools import combinations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[3:10]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = [c for c in s if c.lower() in english_letters]
    palindromes = set()
    for i in range(3, len(s) + 1):
        for combination in combinations(s, i):
            for p in [''.join(p) for p in combinations(combination, len(combination) // 2)]:
                if is_palindrome(p):
                    palindromes.add(p)
    return palindromes