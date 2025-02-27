def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for char in s:
        if char.isalpha():
            for i in range(len(s) - 48):
                substring = s[i:i + 49]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes