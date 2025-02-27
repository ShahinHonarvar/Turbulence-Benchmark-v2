import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:10])
    if len(letters) < 3:
        return set()
    palindromes = {letter * 3 for letter in letters if letter.upper() == letter.lower()}
    for i in range(1, len(letters) - 1):
        for j in range(i + 1, len(letters)):
            palindrome = ''.join(letters[i:j + 1] + letters[i:j + 1][::-1])
            if len(palindrome) >= 3 and palindrome[0].upper() == palindrome[0]:
                palindromes.add(palindrome)
    return palindromes