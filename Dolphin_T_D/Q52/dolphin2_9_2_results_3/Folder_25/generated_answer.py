def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if substring == substring[::-1]:
            palindromes.add(substring.lower())
    return palindromes