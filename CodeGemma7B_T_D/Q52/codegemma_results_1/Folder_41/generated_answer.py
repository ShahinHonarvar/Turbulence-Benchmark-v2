from collections import defaultdict

def palindrome_of_length_n(text):
    set_of_palindromes = set()
    for i in range(len(text) - 59):
        for j in range(i + n, len(text)):
            palindrome = text[i:j]
            palindrome = palindrome.lower()
            if palindrome == palindrome[::-1]:
                set_of_palindromes.add(palindrome)
    return set_of_palindromes