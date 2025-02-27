def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes