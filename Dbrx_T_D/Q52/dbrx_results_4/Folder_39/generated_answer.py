def palindrome_of_length_n(s):
    n = 59
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n].lower()
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes