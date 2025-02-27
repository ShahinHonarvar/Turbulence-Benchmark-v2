def palindromes_of_specific_lengths(s):
    s = s[0:11].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(3, 6):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes