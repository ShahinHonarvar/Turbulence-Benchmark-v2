def palindrome_of_length_n(s):
    n = 59
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes