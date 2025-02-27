def palindromes_of_specific_lengths(s):
    s = s[100:301].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(50, 101):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes