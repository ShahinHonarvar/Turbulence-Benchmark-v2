def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 87):
        substr = s[i:i + 88]
        if len(substr) == 88 and all((char.isalpha() for char in substr)):
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes