from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 8:
        return set()
    letters = s[1:8]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters) + 1):
            palindrome = letters[i:j]
            if len(palindrome) >= 5 and palindrome == palindrome[::-1] and all((palindrome.count(c) <= letters.count(c) for c in set(palindrome))):
                palindromes.add(palindrome)
    return palindromes