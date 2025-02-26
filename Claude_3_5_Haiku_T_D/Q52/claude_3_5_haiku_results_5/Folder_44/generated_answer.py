def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    if len(s) < 445:
        return palindromes
    for i in range(len(s) - 444):
        substring = s[i:i + 445]
        if len(substring) == 445 and substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes