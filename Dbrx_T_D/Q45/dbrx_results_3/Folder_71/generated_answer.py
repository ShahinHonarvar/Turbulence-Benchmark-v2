import re
    from collections import HashSet

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = re.findall('[a-zA-Z]', s[1:4])
    if len(letters) < 2:
        return set()
    palindromes = HashSet()
    for i in range(2, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            candidate = ''.join(letters[j:j + i])
            if is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes