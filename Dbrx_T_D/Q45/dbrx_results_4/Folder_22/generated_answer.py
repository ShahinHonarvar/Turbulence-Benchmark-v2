from collections import defaultdict

def palindromes_between_indices(s: str) -> set:
    letters = set(s.lower()[5:7])
    palindromes = set()
    if len(letters) < 2:
        return palindromes
    for letter in letters:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            palindrome = char + letter + char
            if palindrome in letters or palindrome[0] == palindrome[2]:
                palindromes.add(palindrome)
    return palindromes