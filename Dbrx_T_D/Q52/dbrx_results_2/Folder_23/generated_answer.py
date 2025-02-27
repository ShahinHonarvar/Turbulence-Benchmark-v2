import string

def is_english_letter(character):
    return character.lower() in string.ascii_letters

def find_pivot(s):
    for i in range(len(s) // 2):
        if not is_english_letter(s[i]) or not is_english_letter(s[-(i + 1)]):
            return i
    return len(s) // 2

def expand_palindrome(s, left, right):
    while left >= 0 and right < len(s) and (s[left].lower() == s[right].lower()):
        if right - left + 1 == 69:
            return s[left:right + 1]
        left -= 1
        right += 1
    return None

def palindrome_of_length_n(s, n=69):
    pivots = [find_pivot(s[i:n]) + i for i in range(len(s) - n + 1)]
    palindromes = set()
    for i in pivots:
        palindrome = expand_palindrome(s, i, i)
        if palindrome:
            palindromes.add(palindrome)
    return palindromes