import re
    from collections import Set

def palindromes_between_indices(s):
    letters = set(re.findall('[a-zA-Z]', s[4:10]))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            palindrome = ''.join(sorted(combo))
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes