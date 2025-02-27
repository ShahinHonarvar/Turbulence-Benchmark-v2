from itertools import permutations

def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    substring = s[4:10].lower()
    letters = [ch for ch in substring if ch in english_letters]
    if len(letters) < 5:
        return set()
    result = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                result.add(palindrome)
    return result