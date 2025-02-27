def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                if len(substring) >= 137:
                    palindromes.add(substring)
    return palindromes