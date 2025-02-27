import re

def palindromes_between_indices(s):
    english_letters = set(re.findall('[a-zA-Z]', s[3:10]))
    palindromes = set()
    for length in range(5, min(14, len(english_letters) + 1)):
        for combination in itertools.combinations(english_letters, length):
            palindrome = ''.join(sorted(combination, key=lambda x: x.lower())).capitalize()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes