import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[4:10])
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            palindrome = ''.join(letters[i:j]) + ''.join(letters[i:j][::-1])
            palindromes.add(palindrome.lower())
    return palindromes