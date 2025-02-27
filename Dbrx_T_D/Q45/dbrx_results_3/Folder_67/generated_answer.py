import re
from collections import defaultdict

def palindromes_between_indices(s: str) -> set:
    letters = re.findall('[a-zA-Z]', s[2:7])
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            sub_palindrome = ''.join(letters[i:j + 1]) + ''.join(reversed(letters[i:j + 1]))
            palindromes.add(sub_palindrome.lower())
    return palindromes