def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 9):
        substring = s[i:i + 10].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes