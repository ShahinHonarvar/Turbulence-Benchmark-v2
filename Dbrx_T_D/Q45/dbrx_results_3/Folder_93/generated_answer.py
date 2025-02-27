import re

def palindromes_between_indices(s):
    s = s[2:8].lower()
    english_letters = re.findall('[a-z]', s)
    palindromes = {x for i in range(6, len(english_letters) + 1) for x in {''.join(english_letters[j:k]) for j in range(len(english_letters) - i + 1) for k in range(j + i, len(english_letters) + 1)} if x == x[::-1]}
    return palindromes