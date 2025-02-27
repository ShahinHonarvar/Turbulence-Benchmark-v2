def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1]
            if substr.lower() == substr[-1:0:-1].lower() and substr.isalpha() and (len(substr) >= 144):
                palindromes.add(substr)
    return palindromes