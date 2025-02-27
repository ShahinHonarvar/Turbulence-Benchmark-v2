def palindromes_of_specific_lengths(s):
    s = s[36:93]
    palindromes = set()
    for i in range(len(s)):
        for j in range(10, 36):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.lower() == substring[::-1].lower() and substring.isalpha():
                    palindromes.add(substring)
    return palindromes