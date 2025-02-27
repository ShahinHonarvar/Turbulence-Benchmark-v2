import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:10])
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes