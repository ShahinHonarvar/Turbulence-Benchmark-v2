def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j + 1].lower()
            if substr == substr[::-1] and substr.isalpha():
                if len(substr) >= 35:
                    palindromes.add(substr)
    return palindromes