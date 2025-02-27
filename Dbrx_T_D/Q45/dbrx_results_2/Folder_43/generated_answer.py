from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    chars = [c.lower() for c in s[2:6] if c.lower() in english_letters]
    for i in range(4, len(chars) + 1):
        for j in range(len(chars) - i + 1):
            if j + i <= len(chars):
                palindrome = ''.join(chars[j:j + i])
                if palindrome[::2] == palindrome[1::2][::-1]:
                    palindromes.add(palindrome)
    return palindromes