def palindromes_of_specific_lengths(s):
    s = s[11:88]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(4, 6):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes