import string

def palindromes_between_indices(s):
    english_letters = string.ascii_letters
    s = s[4:10].lower()
    palindromes = {palindrome for palindrome in {s[i:j] for i in range(len(s)) for j in range(i + 4, len(s) + 1)} if palindrome == palindrome[::-1] and all((letter in english_letters for letter in palindrome))}
    return palindromes