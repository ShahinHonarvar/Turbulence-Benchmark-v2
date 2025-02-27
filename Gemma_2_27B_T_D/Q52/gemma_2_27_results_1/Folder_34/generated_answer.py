def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 32):
        substring = s[i:i + 33].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(s[i:i + 33])
    return palindromes