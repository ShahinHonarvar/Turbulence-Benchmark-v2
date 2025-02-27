from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(text):
    text = text.lower()
    if not text or len(text) < 6:
        return set()
    letters = [ch for ch in text if ch in ascii_lowercase and text.index(ch) in range(1, 6)]
    if not letters:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        palindrome = ''.join(perm)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes