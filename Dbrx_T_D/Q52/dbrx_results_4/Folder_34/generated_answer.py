def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 32):
        if s[i:i + 33].lower() == s[i:i + 33].lower()[::-1] and s[i:i + 33].isalpha():
            palindromes.add(s[i:i + 33])
    return palindromes