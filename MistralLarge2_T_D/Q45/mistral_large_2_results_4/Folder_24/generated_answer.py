from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    substring = s[2:10]
    letters = [c for c in substring if c in ascii_letters]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            palindrome = ''.join(p)
            if palindrome.lower() == palindrome.lower()[::-1]:
                palindromes.add(palindrome)
    return palindromes