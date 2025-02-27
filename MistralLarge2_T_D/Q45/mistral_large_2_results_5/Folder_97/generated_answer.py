import re
    from itertools import permutations

def palindromes_between_indices(s):
    substring = re.sub('[^a-zA-Z]', '', s[:5]).lower()
    letters = set(substring)
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for p in permutations(letters, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes