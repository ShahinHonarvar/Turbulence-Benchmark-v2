import string

def palindrome_of_length_n(s):
    letters = string.ascii_lowercase
    palindromes = set()
    for start in range(len(s) - 17):
        substring = s[start:start + 18]
        if substring.lower() == substring.lower()[::-1] and all((c.lower() in letters for c in substring)):
            palindromes.add(substring)
    return palindromes