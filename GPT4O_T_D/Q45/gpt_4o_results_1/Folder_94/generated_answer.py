from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = s[3:5].lower()
    letters = [c for c in substring if c.isalpha()]
    if not letters:
        return set()
    letter_count = Counter(letters)
    mid = None
    half_palindrome = []
    for char, count in letter_count.items():
        if count % 2 == 1:
            if mid is None:
                mid = char
            else:
                return set()
        half_palindrome.extend(char * (count // 2))
    unique_palindromes = set()
    for perm in set(permutations(half_palindrome)):
        half = ''.join(perm)
        palindrome = half + (mid if mid else '') + half[::-1]
        if len(palindrome) >= 3:
            unique_palindromes.add(palindrome)
    return unique_palindromes