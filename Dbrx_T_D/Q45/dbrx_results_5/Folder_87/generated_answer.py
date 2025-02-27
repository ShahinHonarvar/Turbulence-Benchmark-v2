from collections import defaultdict

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[3:10].lower()
    chars = defaultdict(int)
    for char in substr:
        if char in english_letters:
            chars[char] += 1
    palindromes = set()
    for char, count in chars.items():
        if count >= 3:
            palindromes.add(char * count)
        elif count == 2 and chars[char.lower()] == 1:
            palindromes.add(char + char)
        elif count == 1 and is_palindrome(char * 3):
            palindromes.add(char * 3)
        elif count == 1 and chars[char.lower()] == 2 and is_palindrome(char * 3):
            palindromes.add(char * 3)
    return palindromes