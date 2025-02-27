def palindrome_of_length_n(s):
    palindromes = set()
    n = 33
    for i in range(len(s) - n + 1):
        substring = s[i:i + n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes