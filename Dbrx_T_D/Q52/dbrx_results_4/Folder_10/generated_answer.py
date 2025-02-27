def palindrome_of_length_n(s):
    palindromes = set()
    if len(s) < 54 or not s.isalpha():
        return palindromes
    for i in range(len(s) - 53):
        substring = s[i:i + 54].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes