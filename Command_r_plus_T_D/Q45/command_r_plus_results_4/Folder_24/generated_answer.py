import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:10])
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            palindrome = letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes