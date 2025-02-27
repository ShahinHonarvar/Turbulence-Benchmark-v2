def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 93):
        pal = s[i:i + 94]
        if pal == pal[::-1] and pal.isalpha():
            palindromes.add(pal)
    return palindromes