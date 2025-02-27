def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 63):
        substr = s[i:i + 64]
        if all((substr[j] == substr[63 - j] for j in range(32))):
            palindromes.add(substr)
    return palindromes