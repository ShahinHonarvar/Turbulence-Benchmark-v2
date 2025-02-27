import re
    from collections import Set

def palindromes_between_indices(s):
    english_letters = set(re.findall('[a-zA-Z]', s[1:7]))
    result = set()
    for length in range(7, len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, length):
            palindrome = ''.join(sorted(combination))
            if palindrome == palindrome[::-1] and palindrome not in result:
                result.add(palindrome.lower())
    return result