import re
    from itertools import permutations

def palindromes_between_indices(s):
    chars = re.findall('[a-zA-Z]', s[:7])
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            palindrome = ''.join(perm).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes