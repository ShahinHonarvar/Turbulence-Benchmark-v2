from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [char for char in s if char.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for p in permutations(letters):
        if p == p[::-1]:
            palindrome = ''.join(p)
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes