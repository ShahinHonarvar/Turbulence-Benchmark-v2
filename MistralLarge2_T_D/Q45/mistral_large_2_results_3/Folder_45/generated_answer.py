import re

def palindromes_between_indices(s):
    substring = s[5:10]
    letters = re.findall('[a-zA-Z]', substring)
    lower_letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(lower_letters)):
        for j in range(i + 3, len(lower_letters) + 1):
            candidate = lower_letters[i:j]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes