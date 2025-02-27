def palindrome_of_length_n(s):
    n = 60
    length = len(s)
    palindromes = set()
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
            palindromes.add(substr)
    return palindromes