def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 56):
        substring = s[i:i + 57].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes