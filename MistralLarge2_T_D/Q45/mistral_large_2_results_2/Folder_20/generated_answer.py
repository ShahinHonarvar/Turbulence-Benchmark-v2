import re
    from itertools import permutations

def palindromes_between_indices(s):
    substring = re.sub('[^a-zA-Z]', '', s[2:9]).lower()
    unique_chars = set(substring)
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(unique_chars, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes