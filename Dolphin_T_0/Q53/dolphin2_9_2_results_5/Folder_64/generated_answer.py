def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 8, len(s) + 1):
            substring = s[i:j]
            lowercase_substring = substring.lower()
            if lowercase_substring == lowercase_substring[::-1]:
                palindromes.add(substring)
    return palindromes