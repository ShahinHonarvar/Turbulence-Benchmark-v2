def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 36):
        substring = s[i:i + 37]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes