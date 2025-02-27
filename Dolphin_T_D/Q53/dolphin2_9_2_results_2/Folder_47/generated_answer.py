def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(77, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            substr = s[i:i + length].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes