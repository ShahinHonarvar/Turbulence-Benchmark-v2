import re
    from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    english_letters = re.findall('[a-z]', s)
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    indices = frozenset(range(1, 7))
    for i in indices:
        for j in indices:
            if i > j:
                continue
            substring = ''.join(english_letters[i:j + 1])
            if len(substring) < 7:
                continue
            palindrome = substring + substring[-2::-1]
            palindromes.add(palindrome)
    return palindromes