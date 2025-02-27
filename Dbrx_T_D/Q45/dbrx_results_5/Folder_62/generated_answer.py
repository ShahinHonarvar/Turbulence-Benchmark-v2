from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, min(i + 8, len(s))):
            if english_letters.issuperset(s[i:j + 1]):
                palindromes.add(''.join(sorted(s[i:j + 1], reverse=True)) + ''.join(sorted(s[i:j + 1])))
    return {palindrome for palindrome in palindromes if len(palindrome) >= 7}