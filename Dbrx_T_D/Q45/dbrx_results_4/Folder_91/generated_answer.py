import re

def palindromes_between_indices(s):
    s = s[2:7]
    english_letters = re.findall('[a-zA-Z]', s)
    palindromes = {palindrome for i in range(3, len(english_letters) + 1) for j in range(0, len(english_letters) - i + 1) for palindrome in {english_letters[j:j + i][m:] + english_letters[j:j + i][::-1][:m] for m in range(1, i // 2 + 1)}}
    return {palindrome for palindrome in palindromes if palindrome == palindrome.lower()}