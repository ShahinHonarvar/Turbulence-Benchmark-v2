import re

def palindromes_between_indices(s):
    english_letters = re.findall('[a-zA-Z]', s[3:9])
    if len(english_letters) < 4:
        return set()
    palindromes = {letter * 4 for letter in english_letters}
    for i in range(3, 7):
        for j in range(i + 1, 8):
            for k in range(j + 1, 9):
                palindrome = ''.join(sorted(english_letters[i:j] + english_letters[j:k] + english_letters[i:j][::-1]))
                palindromes.add(palindrome)
    return {palindrome for palindrome in palindromes if palindrome == palindrome[::-1]}