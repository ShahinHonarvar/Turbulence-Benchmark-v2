def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 24):
        substring = s[i:i + 25].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes