from sets import Set

def palindrome_of_length_n(s):
    n = 445
    palindromes = Set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes