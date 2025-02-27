import re

def palindromes_between_indices(s):
    chars = re.findall('[a-zA-Z]', s[5:10])
    english_chars = [c.lower() for c in chars if c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    palindromes = set()
    for i in range(5, len(english_chars) + 1):
        for j in range(len(english_chars) - i + 1):
            palindrome = ''.join(english_chars[j:j + i])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes