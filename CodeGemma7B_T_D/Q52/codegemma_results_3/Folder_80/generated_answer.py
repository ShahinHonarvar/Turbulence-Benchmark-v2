def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 275):
        substring = s[i:i + 276]
        if substring == substring[::-1]:
            palindromes.add(substring.lower())
    return palindromes