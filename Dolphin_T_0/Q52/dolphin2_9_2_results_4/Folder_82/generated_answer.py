def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 27):
        substr = s[i:i + 28]
        if substr == substr[::-1] and all((x.isalpha() for x in substr)):
            palindromes.add(substr)
    return palindromes