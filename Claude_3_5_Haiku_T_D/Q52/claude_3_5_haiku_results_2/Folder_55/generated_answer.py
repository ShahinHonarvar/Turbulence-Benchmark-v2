def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 96):
        substr = s[i:i + 97]
        if len(substr) == 97 and substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes