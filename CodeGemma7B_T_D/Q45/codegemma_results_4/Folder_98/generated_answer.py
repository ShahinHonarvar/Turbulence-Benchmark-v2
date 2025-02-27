from itertools import permutations

def palindromes_between_indices(s):
    letters = []
    for char in s[3:6]:
        if 'A' <= char <= 'Z':
            letters.append(char.lower())
        elif 'a' <= char <= 'z':
            letters.append(char)
    if not letters:
        return set()
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes