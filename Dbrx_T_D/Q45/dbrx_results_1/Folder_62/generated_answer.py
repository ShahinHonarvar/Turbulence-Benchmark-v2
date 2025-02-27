import re
    from collections import HashSet

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = HashSet()
    for i in range(min(8, len(s))):
        for j in range(i, min(len(s), i + 7)):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                palindrome = ''.join(sorted(substring))
                palindromes.add(palindrome)
    return {palindrome for palindrome in palindromes if palindrome == palindrome[::-1]}