def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for length in range(122, 0, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            lower_substring = substring.lower()
            if lower_substring == lower_substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes