def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 444):
        substring = s[i:i + 445]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes