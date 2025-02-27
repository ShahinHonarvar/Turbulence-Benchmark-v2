import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:8])
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters) // 2 + 1):
        for j in range(len(letters) - 2 * i):
            palindrome = letters[j:j + i] + letters[j + i:j + 2 * i][::-1]
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
    return palindromes